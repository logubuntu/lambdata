"""
Lambdata - a collection of Data Science helper functions

"""

import pandas as pd
import numpy as np
from .dataframe_helper import reporting_missing_values

test = pd.DataFrame(np.ones(10))


colors = ('Blue', 'Orange', 'Red', 'Green', 'Violet', 'Cyan')

def increment(number):
    """ increasse a number by one """
    return number + 1

def missing_value_report(df):
    """ simple funtion to show null values by column"""
    print(df.isnull().value_counts())

def nonulls(df):
    """ a function to drop all NaNs in a DataFrame"""
    df.dropna(how='any')
