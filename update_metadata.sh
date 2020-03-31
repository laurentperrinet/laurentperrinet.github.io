#!/usr/bin/env bash


echo -e "\033[0;32mupdating metadata...\033[0m"

msg="updating metadata `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi

python3 clean_bibtex.py

cd ../perrinet_curriculum-vitae_tex

git pull ; git commit  -m "$msg" -a ; git push

echo -e "\033[0;32mrecompiling website...\033[0m"

cd ../hugo_academic

# >>> see MAKE NEW_ENTRIES <<<
# o ../perrinet_curriculum-vitae_tex/LaurentPerrinet_*bib
academic import --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_Publications.bib
academic import --publication-dir talk --bibtex  ../perrinet_curriculum-vitae_tex/LaurentPerrinet_Presentations.bib

python3 update_metadata.py

echo -e "\033[0;32mpushing website...\033[0m"
./update_gitpages.sh $msg
