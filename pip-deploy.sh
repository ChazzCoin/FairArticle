#!/bin/zsh

sudo rm -rf dist
sudo rm -rf build
sudo rm -rf FairArticle.egg-info

python3 setup.py sdist
twine upload dist/*