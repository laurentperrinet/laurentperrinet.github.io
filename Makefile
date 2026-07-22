all: gitpages
default: gitpages

update:
	sh update_hugoblox.sh

diff:
	opendiff ../academic-file-converter/academic/import_bibtex.py  scripts/update_metadata.py

gitpages:
	@echo ">>> Committing changes..."
	git add .
	@if [ -z "$(MESSAGE)" ]; then \
		msg="chore: rebuild site ($$(date))"; \
	else \
		msg="$(MESSAGE)"; \
	fi; \
		git commit -m "$$msg"
	@echo ">>> Pushing to GitHub..."
	git push origin main

entries:
	cd scripts; python update_entries.py

new_entries:
	academic import --compact  ../perrinet_curriculum-vitae.tex/LaurentPerrinet_publications.bib content/publication/
	academic import --compact  ../perrinet_curriculum-vitae.tex/LaurentPerrinet_talks.bib content/talk/

metadata:
	cd scripts; sh update_metadata.sh

academic:
	sh update_hugoblox.sh

test:
# 	hugo --gc --cleanDestinationDir
	hugo server --gc --disableFastRender --renderToMemory

clean:
# 	rm -fr  $(TMPDIR)/hugo_cache
	hugo mod clean --all
	hugo mod tidy
	hugo mod get -u ./...
# 	hugo --gc
# 	hugo --cleanDestination-dir
# 	hugo --debug
