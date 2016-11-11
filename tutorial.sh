#!/usr/bin/env sh

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
cd notebook
jupyter notebook
cd ..
deactivate
