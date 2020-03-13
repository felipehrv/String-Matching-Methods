#!/usr/bin/python3
import numpy as np
import scipy.stats as stats
import pandas as pd
import seaborn as sns

iowa_liquor = pd.read_csv('/Users/feliperodriguez/Desktop/Python/Iowa_liquor_sales.csv',encoding='latin1')
d=iowa_liquor.head(10)
print(d)
