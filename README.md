# N-Queens example with AMPL and HiGHS using amplpy

AMPL and all Solvers are now available as Python Packages ([see docs](https://dev.ampl.com/ampl/python.html)). To use them in [streamlit](https://streamlit.io/) you just need to list the modules in the [requirements.txt](requirements.txt) file as follows:
```
--index-url https://pypi.ampl.com # AMPL's Python Package Index
--extra-index-url https://pypi.org/simple
ampl_module_base # AMPL and base tools
ampl_module_highs # HiGHS solver
ampl_module_gurobi # Gurobi solver
amplpy # Python API for AMPL
```

and load them in [streamlit_app.py](streamlit_app.py):
```python
from amplpy import AMPL, modules
modules.load()
```

- Python API documentation: https://amplpy.readthedocs.io/
- Python modules documentation: https://dev.ampl.com/ampl/python.html

## How to run it locally

```bash
$ python -m venv venv
$ sournce venv/bin/activate
$ python -m install -r requirements.txt --upgrade
$ streamlit run streamlit_app.py
```

When you are ready deploy to https://streamlit.io/!
