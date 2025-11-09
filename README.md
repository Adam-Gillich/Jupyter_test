# Jupyter environment for this workspace

This folder contains a starter notebook and minimal instructions to set up a Python environment and run Jupyter.

Files added:

- `StarterNotebook.ipynb` — small demo notebook (numpy, pandas, matplotlib).
- `requirements.txt` — minimal packages to install.

Quick setup (bash):

```bash
# 1) create a virtual environment
python3 -m venv .venv

# 2) activate it
source .venv/bin/activate

# 3) upgrade pip and install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4) start Jupyter Lab
jupyter lab
```

Then open `StarterNotebook.ipynb` from the Jupyter Lab file browser. If you prefer `jupyter notebook`, you can run `jupyter notebook` instead of `jupyter lab`.

Notes:
- If you use Conda, create a Conda env and install the same packages.
- To use the notebook kernel from the venv, ensure `ipykernel` is installed (pip install ipykernel) and add a kernel with `python -m ipykernel install --user --name=myenv`.

Kernel and venv notes
---------------------

- `ipykernel` is included in `requirements.txt` so the virtual environment will register a kernel if you run the install steps in the README.
- I pinned versions in `requirements.txt` to improve reproducibility. If you want the latest packages, remove the `==<version>` pins.

Selecting the kernel in Jupyter
------------------------------

1. Start Jupyter Lab or Notebook:

```bash
source .venv/bin/activate
jupyter lab
```

2. Open `StarterNotebook.ipynb` in the browser.
3. In the top-right kernel/menu area choose `Kernel` -> `Change kernel` and select the kernel named `LaTeX Jupyter (.venv)` (this kernel was registered as part of the setup).

If you don't see the kernel, ensure you installed `ipykernel` inside the venv and ran:

```bash
python -m ipykernel install --user --name=latex-jupyter-venv --display-name="LaTeX Jupyter (.venv)"
```

Troubleshooting: If Jupyter still lists an older kernel or can't start, restart Jupyter Lab and check `jupyter kernelspec list` to confirm the kernel is present.
