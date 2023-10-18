import os
os.environ["R_HOME"] = "C:\\Program Files\\R\\R-4.1.3\\"

import rpy2
from rpy2.robjects import r
from rpy2.robjects.packages import importr

from rpy2.robjects import pandas2ri
pandas2ri.activate()

import rpy2.situation


def r_info():
    for row in rpy2.situation.iter_info():
        print(row)

r_info()