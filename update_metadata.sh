#!/usr/bin/env bash

cd ../perrinet_curriculum-vitae_tex

git pull ; git commit -m ' updating citations  ' -a ; git push

cd ../hugo_academic

ipython3 update_entries.py

./update_gitpages.sh ' updating metadata '
