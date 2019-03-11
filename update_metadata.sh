#!/usr/bin/env bash

python3 clean_bibtex.py

cd ../perrinet_curriculum-vitae_tex

git pull ; git commit -m ' updating citations  ' -a ; git push

cd ../hugo_academic

# academic import --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_Publications.bib
#
# academic import --publication-dir talk --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_Presentations.bib

ipython3 update_entries.py

./update_gitpages.sh ' updating metadata '
