import os
import tempfile
import streamlit as st

from amplpy import AMPL, tools

# tools.install_modules(["coin"], verbose=True)
tools.load_modules(verbose=True)
uuid = os.environ.get("AMPLKEY_UUID")
if uuid is not None:
    tools.activate_license(uuid, verbose=True)


"""
# N-Queens
 
**How can N queens be placed on an NxN chessboard so that no two of them attack each other?**


## Modeling N-Queens with `alldiff`

Constraint `alldiff` enforces a set of integer variables to take distinct values. Using `alldiff`, we can model N-Queens as follows:

```ampl
param n integer > 0; # N-queens
var Row {1..n} integer >= 1 <= n;
s.t. row_attacks: alldiff ({j in 1..n} Row[j]);
s.t. diag_attacks: alldiff ({j in 1..n} Row[j]+j);
s.t. rdiag_attacks: alldiff ({j in 1..n} Row[j]-j);
```
"""

ampl = AMPL()
ampl.eval(
    """
param n integer > 0; # N-queens
var Row {1..n} integer >= 1 <= n;
s.t. row_attacks: alldiff ({j in 1..n} Row[j]);
s.t. diag_attacks: alldiff ({j in 1..n} Row[j]+j);
s.t. rdiag_attacks: alldiff ({j in 1..n} Row[j]-j);
"""
)
ampl.option["solver"] = "highs"
ampl.option["highs_options"] = "outlev=1"

n = st.slider("How many queens?", 2, 25, 8)

ampl.param["n"] = n
output = ampl.get_output("solve;")
solution = ampl.get_data("Row").to_dict()
queens = set((int(r) - 1, int(c) - 1) for c, r in solution.items())

st.write("# Solution")
solution = "#" + " # " * (n) + "#\n"
for r in range(n):
    row = "".join([" Q " if (r, c) in queens else " + " for c in range(n)])
    # st.write(f"`{row}`")
    solution += "#" + row + "#\n"
solution += "#" + " # " * (n) + "#\n"
st.write(f"```\n{solution}\n```")


st.write("# HiGHS output")
st.write(f"```\n{output}\n```")
