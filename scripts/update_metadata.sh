#!/usr/bin/env bash

echo "\033[0;32mupdating metadata...\033[0m"

msg="updating metadata `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi

python ../scripts/clean_bibtex.py

cd ../../perrinet_curriculum-vitae.tex

git pull ; git commit  -m "$msg" -a ; git push

echo "\033[0;32mrecompiling website...\033[0m"

cd ../laurentperrinet.github.io_hugo/scripts
python ../scripts/update_metadata.py

