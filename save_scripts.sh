#!/bin/bash   


cp *.py ./scripts
cp *.sh ./scripts
cd scripts
git status
git add --all
git commit -m "update"
git push