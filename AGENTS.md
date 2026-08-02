# AGENTS. md
## Core Tech Stack
- Hugo + Hugo Blox Builder (Academic CV)
- Tailwind CSS v4
- Metadata sync via Python scripts & BibTeX
## Key Commands
- **Development**:
make test
- **Deployment**:
make gitpages
(commits and pushes to main)
- **Maintenance**:
make clean,
make update
## High-Signal Workflows
### Publication & Talk Metadata
- **Source of Truth**: Metadata for publications (content/publication/') and talks (content/talk/') is derived from BibTeX files in the external directory '../../perrinet_curriculum-vitae.tex'.
- **Update Pipeline**;
scripts/update_metadata. sh
coordinates pulling changes from the tex repo, cleaning BibTeX, and updating site FrontMatter via 'scripts/update_metadata.py.
- **Warning**: Manual edits to publication/talk FrontMatter are likely to be overwritten by the sync pipeline.
## Conventions
& Constraints
### Languages
Default language is English ('config/_default/languages,yaml'), but a significant portion of content (Talks, Publications) is in French. Maintain the existing language of a file when editing
### Code Style & Comments
- **Indentation**: 2 spaces (' editorconfig*).
- **Commenting**: Use concise comments focusing on
*why* logic exists rather than *what* it does. Avoid leaving dead code or commented-out blocks in final files.
### Content Structure
- Core categories:
content/authors/
- Config:
config/_default/hugo.yaml
content/publication/
content/talk/
content/project/, 'content/post/:
(general) and
params. yaml
(site-specific params).