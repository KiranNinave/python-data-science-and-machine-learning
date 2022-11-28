import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z']) # here rows and columns both are series

print(df > 0) # return array of boolean

print(df[df > 0])

print(df[df['W'] > 0]) # apply filter of one column to other column

print(df[(df['W'] > 0) & df['Z'] > 0]) # conditon using multiple columns use berwise operators logic gates operatiors more specifically
# you cannot use python normal and, or operator as it dones not work with series

df.reset_index() # will reset index

df.set_index("W") # will change index column privious index column will get lost