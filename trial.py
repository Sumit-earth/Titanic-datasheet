import numpy as np
import pandas as pd


data=pd.read_csv('train.csv')

print(data.head())


"""
checking the basic info the dataset
"""

print(data.info())


"""
checking for null values
"""


print(data.isnull().sum())