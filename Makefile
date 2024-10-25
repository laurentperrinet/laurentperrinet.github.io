all: gitpages
default: gitpages

update:
	sh update_hugoblox.sh

diff:
	opendiff ../academic-file-converter/academic/import_bibtex.py  scripts/update_metadata.py

gitpages:
	echo ">>> Commit changes to source repo to GitHub..."
	git add .

	msg="rebuilding site `date`"
	if [ $# -eq 1 ]
	then msg="$1"
	fi
	git commit -m "$msg"

	git push origin main

	echo ">>> Deploying updates to GitHub pages repo..."
	
entries:
	cd scripts; python update_entries.py

new_entries:
	academic import --compact  ../perrinet_curriculum-vitae.tex/LaurentPerrinet_publications.bib content/publication/
	academic import --compact  ../perrinet_curriculum-vitae.tex/LaurentPerrinet_talks.bib content/talk/

metadata:
	cd scripts; sh update_metadata.sh

academic:
	sh update_hugoblox.sh

clean:
	# rm -fr  $(TMPDIR)/hugo_cache
	hugo mod clean --all
	hugo mod tidy
	hugo mod get -u ./...
	# hugo --gc
	# hugo --cleanDestinationDir
	# hugo --debug
	