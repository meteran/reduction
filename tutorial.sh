#!/usr/bin/env sh

mkdir dimensionality_reduction
cd dimensionality_reduction
if [ `command -v pyvenv` ]; then
	VENV=pyvenv
elif [ `command -v virtualenv` ]; then
	VENV=virtualenv
elif [ `command -v venv` ]; then
	VENV=venv
else
	echo "no virtualenv"
fi
$VENV --system-site-packages venv
source venv/bin/activate
python -m pip install jupyter
jupyter notebook
deactivate
cd ..
#rm -r dimensionality_reduction
