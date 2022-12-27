import os
import tempfile
import streamlit as st

from amplpy import AMPL, tools

# tools.install_modules(["coin"], verbose=True)
tools.load_modules(verbose=True)
uuid = os.environ.get("AMPLKEY_UUID")
if uuid is not None:
    tools.activate_license(uuid, verbose=True)

ampl = AMPL()
ampl.eval(
    """
set I := 1..1000;
var x{I} binary;
param v{i in I} := 1 + Irand224() mod 1000;
param w{i in I} := 1 + Irand224() mod 1000;
maximize profit: sum{i in I} v[i] * x[i];
s.t. capacity: sum{i in I} w[i] * x[i] <= 1000;
"""
)
ampl.option["solver"] = "highs"

## Version

st.write(ampl.option["version"])

## Solve

st.write(ampl.get_output("solve;"))
