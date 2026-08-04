import subprocess
from pathlib import Path

# The commit hash before we started refactoring/sanitizing a lot
SAFE_COMMIT = "08a9724ad"

def get_git_content(file_path, commit=SAFE_COMMIT):
    try:
        return subprocess.check_output(['git', 'show', f'{commit}:{file_path}'], encoding='utf-8')
    except Exception:
        return None

def extract_block(content, key):
    if not content or '---' not in content: return None
    parts = content.split('---')
    if len(parts) < 2: return None
    fm = parts[1].split('\n')
    
    block = []
    found = False
    for line in fm:
        if line.strip() == f'{key}:':
            found = True
            block.append(line)
            continue
        if found:
            # A block continues as long as lines start with whitespace, 
            # are empty, or are list items starting with '-'
            if line.startswith(' ') or not line.strip() or line.startswith('- '):
                block.append(line)
            else:
                break
    return '\n'.join(block) if block else None

def restore_metadata(p, keys):
    current_content = p.read_text(encoding='utf-8')
    git_content = get_git_content(str(p))
    if not git_content: return False
    
    parts = current_content.split('---')
    if len(parts) < 3: return False
    fm_lines = parts[1].split('\n')
    
    changed = False
    # To avoid multiple passes, we process the FM lines and replace blocks
    # We'll do it key by key for simplicity in this script
    for key in keys:
        original_block = extract_block(git_content, key)
        if not original_block: continue
        
        new_fm_lines = []
        skip = False
        found_in_current = False
        for line in fm_lines:
            if line.strip() == f'{key}:':
                found_in_current = True
                new_fm_lines.append(original_block)
                skip = True
            elif skip:
                if line.startswith(' ') or not line.strip() or line.startswith('- '):
                    continue
                else:
                    skip = False
                    new_fm_lines.append(line)
            else:
                new_fm_lines.append(line)
        
        if not found_in_current:
            # Insert the block before the final delimiter if missing
            new_fm_lines.append('')
            new_fm_lines.append(original_block)
        
        fm_lines = new_fm_lines
        changed = True

    final_content = '---' + '\n'.join(fm_lines) + '---' + '\n'.join(parts[2:])
    if final_content != current_content:
        p.write_text(final_content, encoding='utf-8')
        return True
    return False

# Define target directories and keys to restore
targets = [
    'content/publication',
    'content/post',
    'content/authors'
]
keys_to_restore = ['authors', 'grants']
total = 0

for target in targets:
    path = Path(target)
    if not path.exists(): continue
    for p in path.rglob('*.md'):
        if restore_metadata(p, keys_to_restore):
            total += 1

print(f"Total files restored: {total}")
