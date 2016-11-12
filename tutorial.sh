#!/usr/bin/env bash

if [ `command -v pyvenv` ]; then
    VENV=pyvenv
elif [ `command -v virtualenv` ]; then
    VENV=virtualenv
elif [ `command -v venv` ]; then
    VENV=venv
else
    echo "no virtualenv"
    exit
fi
VENV_DIR=.venv
$VENV --system-site-packages $VENV_DIR
source $VENV_DIR/bin/activate
python -m pip install -r requirements.txt
PYTHONPATH=`pwd`:$PYTHONPATH
echo $PYTHONPATH
jupyter notebook
deactivate
