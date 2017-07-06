#!/bin/bash   


cp *.py ./scripts
cp *.sh ./scripts
cd scripts
git status
git add --all
git commit -m "removed some unwanted functions from one_script"
git status
git push

echo 'added'
ls *.py *.sh
