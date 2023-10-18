from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import matplotlib.pyplot as plt

import pandas as pd
import xarray as xr
import numpy as np
import seaborn as sns

import matplotlib

print("pd", pd.__version__)
print("xr", xr.__version__)
print("np", np.__version__)
print("sns", sns.__version__)

sns.set_style('whitegrid')
matplotlib.rcParams['figure.figsize'] = (15, 10)
