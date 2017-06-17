#!/bin/bash
PS1=$
virtualenv venv --python=python3
source ./venv/bin/activate
pip install -r requirements.txt
vagrant up
python code/config_g1.py
#python code/config_g2.py
python code/config_g3.py
