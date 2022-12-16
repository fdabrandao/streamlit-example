import os
import tempfile
import streamlit as st

from amplpy import AMPL
import ampl_base, ampl_highs


def activate_license(uuid):
    from urllib.request import urlretrieve

    uuid = uuid.strip()
    url = "https://portal.ampl.com/download/license/{}/ampl.lic".format(uuid)
    tmpfile = tempfile.mktemp(".lic")
    urlretrieve(url, tmpfile)
    os.environ["AMPL_LICFILE"] = tmpfile
    os.environ["AMPLKEY_RUNTIME_DIR"] = tempfile.mkdtemp()


uuid = os.environ.get("AMPLKEY_UUID")
if uuid is not None:
    activate_license(uuid)

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
