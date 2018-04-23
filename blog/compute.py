from __future__ import print_function

import datetime as dt
from datetime import datetime

import numpy as np
#import pandas.io.data as web
from scipy.stats import norm
import pandas_datareader.data as web


def compute(P, c, mu, sigma):
    """
    Variance-Covariance calculation of daily Value-at-Risk
    using confidence level c, with mean of returns mu
    and standard deviation of returns sigma, on a portfolio
    of value P.
    """
    alpha = norm.ppf(1-c, mu, sigma)
    return P - P*(alpha + 1)
