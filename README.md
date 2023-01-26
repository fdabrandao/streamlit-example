# N-Queens example with AMPL and HiGHS using amplpy

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/fdabrandao/streamlit-nqueens/)

[AMPL and all Solvers are now available as Python Packages](https://dev.ampl.com/ampl/python.html). To use them in [streamlit](https://streamlit.io/) you just need to list the modules in the [requirements.txt](requirements.txt) file as follows:
```
--index-url https://pypi.ampl.com # AMPL's Python Package Index
--extra-index-url https://pypi.org/simple
ampl_module_base # AMPL
ampl_module_highs # HiGHS solver
ampl_module_gurobi # Gurobi solver
amplpy # Python API for AMPL
```

and load them in [streamlit_app.py](streamlit_app.py):
```python
from amplpy import AMPL, modules
modules.load()
ampl = AMPL()
```

- Python API documentation: https://amplpy.readthedocs.io/
- Python modules documentation: https://dev.ampl.com/ampl/python/

## How to run it locally

```bash
$ python -m venv venv
$ sournce venv/bin/activate
$ python -m install -r requirements.txt --upgrade
$ streamlit run streamlit_app.py
```

When you are ready deploy to https://streamlit.io/! This app is running there: https://share.streamlit.io/fdabrandao/streamlit-nqueens/