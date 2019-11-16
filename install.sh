#!/usr/bin/env bash

echo "Installing microkg..."

pipenv --rm
pipenv install
pipenv run flit install --symlink

ln -sf `pipenv run pyenv which "microkg"` "$HOME/bin/microkg"
