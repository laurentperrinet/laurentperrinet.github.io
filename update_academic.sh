#!/usr/bin/env bash

python3 clean_bibtex.py

# Display available updates to Academic.
cd themes/academic
git fetch
#git log --pretty=oneline --abbrev-commit --decorate HEAD..origin/master
cd ../../

# Update Academic.
git submodule update --remote --merge themes/academic
