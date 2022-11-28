# a dataframe is bunch of series sharing same index

import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z']) # here rows and columns both are series

print(df) # contains pandas series
print("type df", type(df)) # <class 'pandas.core.frame.DataFrame'>

print(df['W']) # pandas series, also can write df.W
print("type df['W']", type(df['W'])) # <class 'pandas.core.series.Series'>

print(df['W']['A']) # float value

print(df[['W', 'Z']]) # return multiple columns as df

df['new'] = df['W'] + df['Z'] # creating new column from existing operations on df
print(df) 

df.drop("new", axis=1, inplace=True) # droping column, we have to specify axis, need to specify inplace for mutations


print(df.loc['C']) # selecting row it's series

print(df.iloc[2]) # selecting row by index positions 

print(df.loc['B', 'Y']) # select value from row and column

print(df.loc[['A', 'B'], ['W', 'Y']]) # multiple row and column