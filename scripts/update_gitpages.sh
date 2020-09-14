#!/bin/bash

# see https://gohugo.io/hosting-and-deployment/hosting-on-github/
cd ..

echo ">>> Commit changes to source repo to GitHub..."

git add .

msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

git push origin master


echo ">>> Deploying updates to GitHub pages repo..."

# Build the project.
hugo

# Go To Public folder
cd laurentperrinet.github.io
# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -am "$msg"

# Push source and build repos.
git push origin master

# Come Back up to the Project Root
cd ..
