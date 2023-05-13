#!/bin/bash

if command -v python3 &>/dev/null; then
    echo "Python is installed."
else
    echo "Python is not installed."
fi

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m pip install colorama tabulate
pytest src
python3 main.py
deactivate