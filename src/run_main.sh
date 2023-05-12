#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip install colorama tabulate
pytest src
python3 main.py
deactivate