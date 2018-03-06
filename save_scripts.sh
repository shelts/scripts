#!/bin/bash   

cp nbody_functional.py nbody_tools
cp one_script.py nbody_tools
cp nbody_useful_plots.py nbody_tools
cp *.py ./scripts
cp *.sh ./scripts
cd scripts
git status
git add --all
git commit -m "update"
git status
git push

