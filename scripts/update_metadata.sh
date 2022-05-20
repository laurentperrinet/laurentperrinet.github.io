#!/usr/bin/env bash

echo "\033[0;32mupdating metadata...\033[0m"

msg="updating metadata `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi

python3 ../scripts/clean_bibtex.py

cd ../../perrinet_curriculum-vitae_tex

git pull ; git commit  -m "$msg" -a ; git push

echo "\033[0;32mrecompiling website...\033[0m"

cd ../hugo_academic/scripts

# >>> see MAKE NEW_ENTRIES <<<
# o ../perrinet_curriculum-vitae_tex/LaurentPerrinet_*bib
# academic import --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_publications.bib
# academic import --publication-dir content/talk --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_talks.bib

python3 ../scripts/update_metadata.py

#echo "\033[0;32mpushing website...\033[0m"
#sh ../scripts/update_gitpages.sh $msg
