default: gitpages

update:
	hugo mod get github.com/wowchemy/wowchemy-hugo-modules/wowchemy/@master
	git submodule update --init --recursive
	git pull

gitpages:
	cd laurentperrinet.github.io; git checkout master; 	git pull
	cd scripts; sh update_gitpages.sh

entries:
	cd scripts; python update_entries.py

new_entries:
	academic import --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_Publications.bib
	academic import --publication-dir talk --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_Presentations.bib

metadata:
	cd scripts; sh update_metadata.sh

academic:
	sh update_academic.sh
