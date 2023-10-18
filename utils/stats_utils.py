import statsmodels.api as sm
import scipy
import numpy as np
import pandas as pd


def r_to_z(r):
    return np.log((1 + r) / (1 - r)) / 2.0


def z_to_r(z):
    e = np.exp(2 * z)
    return (e - 1) / (e + 1)


def corr_ci(r, n, alpha=0.05):
    z = r_to_z(r)
    se = 1.0 / np.sqrt(n - 3)
    z_crit = scipy.stats.norm.ppf(1 - alpha/2)  # 2-tailed z critical value

    lo = z - z_crit * se
    hi = z + z_crit * se

    return z_to_r(lo), z_to_r(hi)

