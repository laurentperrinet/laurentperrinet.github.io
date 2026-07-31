import os
import re
import yaml

MAPPING = {
    "motion detection": "motion-detection",
    "motion-clouds": "motion-detection",
    "motion prediction": "motion-detection",
    "eye movements": "eye-movements",
    "Bayesian model": "bayesian-modeling",
    "sparse coding": "sparse-coding",
    "efficient coding": "efficient-coding",
    "coding decoding": "coding-decoding",
    "area-v1": "visual-cortex",
    "lateral connections": "visual-cortex",
    "center-surround interactions": "visual-cortex",
    "neuromorphic hardware": "neuromorphic-hardware",
    "Biologically Inspired Computer vision": "vision"
}

MAPPING_LOWER = {k.lower(): v for k, v in MAPPING.items()}
REDUNDANT = {"grant", "past-grant", "current-grant", "events", "computational neuroscience"}

def kebab_case(s):
    return s.lower().replace(" ", "-")

def transform_tags(tags):
    if tags is None:
        return None
    if isinstance(tags, str):
        tags = [tags]
    if not isinstance(tags, list):
        return tags
    new_tags = []
    for tag in tags:
        if not isinstance(tag, str):
            continue
        tag_lower = tag.lower()
        if tag_lower in MAPPING_LOWER:
            tag = MAPPING_LOWER[tag_lower]
        if tag.lower() in REDUNDANT:
            continue
        tag = kebab_case(tag)
        new_tags.append(tag)
    seen = set()
    final_tags = []
    for t in new_tags:
        if t not in seen:
            final_tags.append(t)
            seen.add(t)
    return final_tags

def process_files():
    dirs = [
        "content/post/",
        "content/publication/",
        "content/talk/",
        "content/project/",
        "content/grant/"
    ]
    modified_count = 0
    examples = []
    for d in dirs:
        if not os.path.exists(d):
            continue
        for root, _, files in os.walk(d):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
                    if not match: continue
                    frontmatter_str, body = match.groups()
                    try:
                        frontmatter = yaml.safe_load(frontmatter_str)
                    except yaml.YAMLError: continue
                    if not frontmatter or 'tags' not in frontmatter: continue
                    old_tags = frontmatter['tags']
                    new_tags = transform_tags(old_tags)
                    if old_tags != new_tags:
                        frontmatter['tags'] = new_tags
                        # Preserve order and avoid sorting keys
                        new_frontmatter_str = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False).strip()
                        new_content = f"---\n{new_frontmatter_str}\n---\n{body}"
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        modified_count += 1
                        if len(examples) < 5:
                            examples.append((file_path, old_tags, new_tags))
    return modified_count, examples

if __name__ == "__main__":
    count, ex = process_files()
    print(f"MODIFIED_COUNT:{count}")
    for path, old, new in ex:
        print(f"EXAMPLE:File:{path}|Before:{old}|After:{new}")
