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
$VENV --system-site-packages venv
source venv/bin/activate
python -m pip install -r requirements.txt
jupyter notebook
deactivate
