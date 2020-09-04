default: gitpages

gitpages:
	sh scripts/update_gitpages.sh

entries:
	python3 scripts/update_entries.py

new_entries:
	academic import --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_Publications.bib
	academic import --publication-dir talk --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_Presentations.bib

metadata:
	sh scripts/update_metadata.sh

academic:
	sh scripts/update_academic.sh
