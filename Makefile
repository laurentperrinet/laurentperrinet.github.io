default: metadata

gitpages:
	sh ./update_gitpages.sh

entries:
	python3 ./update_entries.py

new_entries:
	academic import --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_Publications.bib
	academic import --publication-dir talk --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_Presentations.bib

metadata:
	sh ./update_metadata.sh
