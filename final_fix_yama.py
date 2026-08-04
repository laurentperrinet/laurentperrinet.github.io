import subprocess
from pathlib import Path
import yaml

SAFE_COMMIT = "08a9724ad"

def get_git_raw(file_path):
    try:
        return subprocess.check_output(['git', 'show', f'{SAFE_COMMIT}:{file_path}'], encoding='utf-8')
    except Exception: return None

def extract_authors_from_git(content):
    if not content or '---' not in content: return None
    parts = content.split('---')
    fm = parts[1].split('\n')
    block = []
    found = False
    for line in fm:
        if line.strip() == 'authors:':
            found = True; block.append(line)
            continue
        if found:
            if line.startswith(' ') or not line.strip() or line.startswith('- '): block.append(line)
            else: break
    return '\n'.join(block) if block else None

def extract_grants_from_git(content):
    if not content or '---' not in content: return None
    parts = content.split('---')
    fm = parts[1].split('\n')
    # Find grants key OR orphans that look like grants
    found_key = False
    grants_list = []
    for line in fm:
        if line.strip() == 'grants:':
            found_key = True; grants_list.append(line)
            continue
        if found_key:
            if line.startswith(' ') or not line.strip() or line.startswith('- '): grants_list.append(line)
            else: break
    
    if not found_key:
        orphans = [l for l in fm if l.strip().startswith('- ') and any(x in l for x in ['codde', 'brain-scales', 'facets', 'anr-'])]
        if orphans: return 'grants:\n' + '\n'.join(orphans)
    return '\n'.join(grants_list) if grants_list else None

def process_file(p):
    current = p.read_text(encoding='utf-8')
    git = get_git_raw(str(p))
    if not git: return False
    
    parts = current.split('---')
    if len(parts) < 3: return False
    fm_lines = parts[1].split('\n')
    
    # Restore Authors
    orig_authors = extract_authors_from_git(git)
    if orig_authors:
        new_fm = []
        skip = False
        found = False
        for line in fm_lines:
            if line.strip() == 'authors:':
                found = True; new_fm.append(orig_authors); skip = True
            elif skip:
                if not (line.startswith(' ') or not line.strip() or line.startswith('- ')):
                    skip = False; new_fm.append(line)
            else: new_fm.append(line)
        if not found: new_fm.insert(0, orig_authors + '\n')
        fm_lines = new_fm

    # Restore Grants
    orig_grants = extract_grants_from_git(git)
    if orig_grants:
        new_fm = []
        skip = False
        found = False
        for line in fm_lines:
            if line.strip() == 'grants:':
                found = True; new_fm.append(orig_grants); skip = True
            elif skip:
                if not (line.startswith(' ') or not line.strip() or line.startswith('- ')):
                    skip = False; new_fm.append(line)
            else: new_fm.append(line)
        if not found:
            new_fm.append('') # spacer
            new_fm.append(orig_grants)
        fm_lines = new_fm

    final_content = '---' + '\n'.join(fm_lines).strip() + '\n---\n' + '\n'.join(parts[2:])
    if final_content != current:
        p.write_text(final_content, encoding='utf-8')
        return True
    return False

for target in ['content/publication', 'content/post', 'content/authors']:
    path = Path(target)
    if not path.exists(): continue
    for p in path.rglob('*.md'):
        process_file(p)
