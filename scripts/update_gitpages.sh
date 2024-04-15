#!/bin/bash

# see https://gohugo.io/hosting-and-deployment/hosting-on-github/
# https://wowchemy.com/docs/deployment/

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

# # Build the project.
# hugo

# # Go To Public folder
# cd public
# # Add changes to git.
# git add .

# # Commit changes.
# msg="rebuilding site `date`"
# if [ $# -eq 1 ]
#   then msg="$1"
# fi
# git commit -am "$msg"

# # Push source and build repos.
# git push origin main

# # Come Back up to the Project Root
# cd ..
