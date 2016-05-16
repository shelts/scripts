#!/bin/bash



cd BOINC
git status
git add --all
git commit -m "automated update in process of debugging"

cd ..
cd milkywayathome_client/boinc/boinc
git fetch
git merge
cd ..
cd ..
git diff --submodule
git add --all
git commit -m "automated update in the process of debugging submodule BOINC"
git push
 "-DBOINC_APPLICATION=ON"
 "-DCMAKE_BUILD_TYPE=Release"