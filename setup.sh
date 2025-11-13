#!/usr/bin/env bash
mkdir venv;
python3 -m venv venv/;
./venv/bin/pip install arguably GitPython PyGithub requests;
chmod +x *.py;
echo "youre all set!"
