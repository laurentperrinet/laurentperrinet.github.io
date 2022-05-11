default: gitpages

update:
	sh update_wowchemy.sh

diff:
	opendiff ../academic-admin/academic/import_bibtex.py  scripts/update_metadata.py
gitpages:
	cd public; git checkout master; git pull
	cd scripts; sh update_gitpages.sh

entries:
	cd scripts; python update_entries.py

new_entries:
	academic import --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_Publications.bib
	academic import --publication-dir talk --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_talks.bib

metadata:
	cd scripts; sh update_metadata.sh

academic:
	sh update_wowchemy.sh
