# PYTHON Fundamentals and core



## Important Python Commands

#### Check installed versions

```bash
python --version
pip --version
```

- `python --version`: Displays the installed Python version.
- `pip --version`: Displays the installed `pip` version and its location.

#### Upgrade pip and install NumPy

```bash
```bash
python filename.py
```

- `pip install --upgrade pip`: Updates `pip` to the latest available version.
- `pip install numpy`: Downloads and installs the NumPy package in the active
	Python environment.

Runs the specified Python file. Python interprets and executes the code; it
does not compile the file as a separate step.

#### Create a virtual environment

```bash
python -m venv env
# Or, on Windows:
py -m venv env
```

Creates an isolated Python environment named `env` for the project.

#### Activate a virtual environment on Windows

```bat
env\Scripts\activate.bat
```

Activates the `env` virtual environment in Command Prompt. After activation,
packages installed with `pip` are installed in that environment.

- activate for mac or linux
- activate.bat : for windows cmd
- activate.ps1 : for windows powershell
- activate.fish : for fish shell on linux or mac

#### Install and upgrade pip and Numpy
pip install --upgrade pip
pip install numpy


#### Verify the Installation

```
python -c "import numpy as np; print('NumPy Version:', np.__version__)"
```


deactivate : to deactivate env

pip freeze > requirements.txt :  save your package list.

pip install -r requirements.txt : Anyone else can then replicate your environment 


