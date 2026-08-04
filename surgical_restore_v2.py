import subprocess
from pathlib import Path

# Prior commit where grants/authors were roughly correct, 
# though some had orphaned list items that the current aeffe75fd should be compared to.
SAFE_COMMIT = "08a9724ad"

def get_git_content(file_path, commit=SAFE_COMMIT):
    try:
        return subprocess.check_output(['git', 'show', f'{commit}:{file_path}'], encoding='utf-8')
    except Exception:
        return None

def extract_grants_from_raw(content):
    """Specifically handles the case where grants might be orphaned list items."""
    if not content or '---' not in content: return None
    parts = content.split('---')
    fm = parts[1].split('\n')
    
    grants = []
    found_key = False
    # We look for "grants:" but also identify list items that SHOULD be grants 
    # by checking if they were in the 'safe' version and are now missing.
    for line in fm:
        if line.strip() == 'grants:':
            found_key = True
            grants.append(line)
            continue
        if found_key:
            if line.startswith(' ') or not line.strip() or line.startswith('- '):
                grants.append(line)
            else:
                break
    
    # HEURISTIC: If no 'grants:' key was found, but there are orphaned list items 
    # that look like grants (e.g., - codde, - brain-scales), we capture them.
    if not found_key:
        orphans = []
        for line in fm:
            if line.strip().startswith('- ') and any(x in line for x in ['codde', 'brain-scales', 'facets', 'anr-']):
                orphans.append(line)
        if orphans:
            return 'grants:\n' + '\n'.join(orphans)
            
    return '\n'.join(grants) if grants else None

def extract_authors(content):
    if not content or '---' not in content: return None
    parts = content.split('---')
    fm = parts[1].split('\n')
    block = []
    found = False
    for line in fm:
        if line.strip() == 'authors:':
            found = True
            block.append(line)
            continue
        if found:
            if line.startswith(' ') or not line.strip() or line.startswith('- '):
                block.append(line)
            else:
                break
    return '\n'.join(block) if block else None

def restore_metadata(p):
    current_content = p.read_text(encoding='utf-8')
    git_content = get_git_content(str(p))
    if not git_content: return False
    
    parts = current_content.split('---')
    if len(parts) < 3: return False
    fm_lines = parts[1].split('\n')
    
    changed = False
    
    # Restore Authors
    orig_authors = extract_authors(git_content)
    if orig_authors:
        new_fm = []
        skip = False
        found = False
        for line in fm_lines:
            if line.strip() == 'authors:':
                found = True
                new_fm.append(orig_authors)
                skip = True
            elif skip:
                if line.startswith(' ') or not line.strip() or line.startswith('- '): continue
                else:
                    skip = False
                    new_fm.append(line)
            else:
                new_fm.append(line)
        if not found:
            new_fm.insert(0, orig_authors + '\n')
        fm_lines = new_fm
        changed = True

    # Restore Grants (handling orphans from git version)
    orig_grants = extract_grants_from_raw(git_content)
    if orig_grants:
        new_fm = []
        skip = False
        found = False
        for line in fm_lines:
            if line.strip() == 'grants:':
                found = True
                new_fm.append(orig_grants)
                skip = True
            elif skip:
                if line.startswith(' ') or not line.strip() or line.startswith('- '): continue
                else:
                    skip = False
                    new_fm.append(line)
            else:
                new_fm.append(line)
        if not found:
            # Insert grants before the end of FM
            new_fm.append('')
            new_fm.append(orig_grants)
        fm_lines = new_fm
        changed = True

    final_content = '---' + '\n'.join(fm_lines) + '---' + '\n'.join(parts[2:])
    if final_content != current_content:
        p.write_text(final_content, encoding='utf-8')
        return True
    return False

targets = ['content/publication', 'content/post', 'content/authors']
total = 0
for target in targets:
    path = Path(target)
    if not path.exists(): continue
    for p in path.rglob('*.md'):
        if restore_metadata(p):
            total += 1

print(f"Total files restored: {total}")
