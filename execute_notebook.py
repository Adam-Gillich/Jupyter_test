#!/usr/bin/env python3
"""
Execute the StarterNotebook.ipynb using nbclient and write an executed copy.

Usage: run this with the project's venv Python so the same environment and kernel are available.
Example:
    /home/adam/work/Jupyter/.venv/bin/python execute_notebook.py
"""
from pathlib import Path
from nbformat import read, write
from nbclient import NotebookClient

# nbclient moved exceptions in some versions; prefer the exceptions submodule but
# fall back to a lightweight local definition if it's not present.
try:
    from nbclient.exceptions import CellExecutionError
except Exception:
    class CellExecutionError(Exception):
        """Fallback CellExecutionError if nbclient.exceptions isn't available."""
        pass

ROOT = Path(__file__).parent
NB_IN = ROOT / "StarterNotebook.ipynb"
NB_OUT = ROOT / "StarterNotebook-executed.ipynb"

def main():
    if not NB_IN.exists():
        print(f"Input notebook not found: {NB_IN}")
        raise SystemExit(2)

    with NB_IN.open("r", encoding="utf-8") as f:
        nb = read(f, as_version=4)

    # Use the kernel we registered earlier (user kernelspec name)
    kernel_name = "latex-jupyter-venv"
    client = NotebookClient(nb, timeout=120, kernel_name=kernel_name)

    try:
        print(f"Executing {NB_IN} with kernel '{kernel_name}' ...")
        client.execute()
    except CellExecutionError as e:
        print("Notebook execution failed on a cell:", e)
        # write partial output for debugging
        with NB_OUT.open("w", encoding="utf-8") as f:
            write(nb, f)
        print(f"Wrote partial output to {NB_OUT}")
        raise

    # write executed notebook
    with NB_OUT.open("w", encoding="utf-8") as f:
        write(nb, f)

    print(f"Notebook executed successfully. Wrote: {NB_OUT}")

if __name__ == "__main__":
    main()
