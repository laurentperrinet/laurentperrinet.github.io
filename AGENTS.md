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

### Global Metadata Architecture
To maintain site coherence, all metadata must be selected from these controlled vocabularies. Do not create new categories/projects without updating this file.

#### 1. Categories (Overarching Scientific Domains)
Select one or more based on the primary contribution of the work:
- `Theoretical Neuroscience`: Mathematical frameworks, abstract proofs, formal models.
- `Biological Neuroscience`: Biological implementation, physiology, animal data.
- `Behavioural Neuroscience`: Human experiments, psychological studies, perception tests.
- `Computational Neuroscience`: Bridge category; simulation and algorithmic modeling of brain function.
- `Visual Neuroscience`: Focus on the visual system's functional/biological properties.
- `NeuroAI & Machine Learning`: Actual AI architectures, neuromorphic hardware, or ML optimization.
- `Computer Vision`: Computer vision algorithms, benchmarks, and image processing tools.
- `Clinical Neuroscience`: Medical/clinical applications (Specialty).
- `Education`: Courses, teaching material, PhD training.
- `Outreach & Public Engagement`: Dissemination to the general public, museums, forums.

#### 2. Tags (Topics & Tooling)
Use kebab-case for all tags.
- **Retinotopy Cluster**: Must apply as a set: `{ "retinotopy", "log-polar-mapping", "foveated-vision" }`.
- **Tooling & Methods**: `pynn`, `motion-clouds`, `deep-learning` (if using PyTorch/TF/JAX), `log-gabor`, `homeostasis`.
- **Conceptual Clusters**: `sparse-coding`, `eye-movements`, `primary-visual-cortex`, `predictive-coding`, `spiking-neural-networks`, `neuromorphic-computing`, `visual-illusions`, `metaplasticity`, `motion-perception` (cognitive), `motion-detection` (low-level), `temporal-coding`, `motion-anticipation`, `bayesian-modelling`.

#### 3. Projects (Thematic Pillars)
Link works to one of these core projects via the `projects:` field:
- `art-science`: Collaborative art, exhibitions (e.g., Étienne Rey), and museum work.
- `open-science`: Open source software (MotionClouds), open data, reproducibility.
- `tout-public`: Content specifically designed for a non-specialist audience.

#### 4. Grants & Author Logic
- **Grants**: Must use the `grants:` key followed by a list of identifiers (e.g., `- facets`). Never leave orphaned grant items without the key.
- **Author Profiles**:
    - `laurent-u-perrinet`: Assign all overarching scientific categories.
    - Others: Select a representative set (3-4) based on weighted frequency in their co-authored works.
- **Coherence Sync**: Metadata (categories, tags, projects) must be mirrored identicaly between any `talk/` entry and its corresponding `slides/`.
