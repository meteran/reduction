# Dimensionality Reduction

## Creating environment
  * With _docker_:
    1. `docker pull continuumio/anaconda3` or if you have not enough disk space `docker pull continuumio/miniconda3`
    1. `docker run --rm -i -t -p 8888:8888 continuumio/anaconda3 /bin/bash` or `docker run --rm -i -t -p 8888:8888 continuumio/miniconda3 /bin/bash` 
    1. Go to `Running` step

  * With _virtualenv_:
    1. `python3 -m venv --system-site-packages .bigdata_venv` or if you are using python2 `python -m virtualenv --system-site-packages .bigdata_venv` 
    1. `source .bigdata_venv/bin/activate` or on _Windows_ `.bigdata_venv\Scripts\activate.bat`
    1. Go to `Running` step
    
    Note: When you finished don't forget `deactivate` command or on _Windows_ `.bigdata_venv\Scripts\deactivate.bat`

## Running
  1. `git clone https://github.com/meteran/reduction.git big_data_dr`
  1. `cd big_data_dr`
  1. `./tutorial.sh` or on Windows `tutorial.bat` (Note: if it does not work, you should find compiled versions of the libraries from `requirements.txt`)
  1. Wait until everything is installed, and you see something like this: `[I 14:25:41.032 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).`.
  1. Now you should be redirected to web browser with _jupyter notebook_ opened. If it does not go to `http://localhost:8888`.
  1. Open `notebooks` directory and choose `Dimensionality Reduction.ipynb` notebook.

