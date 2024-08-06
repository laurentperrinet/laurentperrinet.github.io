#!/bin/bash

# see https://docs.hugoblox.com/getting-started/install-hugo/#deploy

# got to root folder
cd ..

echo ">>> Commit changes to source repo to GitHub..."

git add .

msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

git push origin main


echo ">>> Deploying updates to GitHub pages repo..."
