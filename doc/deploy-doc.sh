#!/usr/bin/env sh

make html
git clone git@github.com:hadim/pygraphml.git gh-pages
cd gh-pages/
git co gh-pages
git rm -fr .
cp -R ../build/html/* .
touch .nojekyll
git add . --all
git commit -am "deploy doc"
git push
