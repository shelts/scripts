#!/bin/bash   

cp create_data_hist/*.py ./scripts/create_data_hist/
cp *.py ./scripts
cp *.sh ./scripts
cd scripts
git status
git add --all
git commit -m "update"
git status
git push

