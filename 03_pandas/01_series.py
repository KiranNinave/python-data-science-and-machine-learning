# is series is pands ds which is a numpy array with lables

import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

data_without_lables = pd.Series(data=my_data) # here keys are 0,1,2 like indexs
print("data_without_lables", data_without_lables)

data_with_labels = pd.Series(data=my_data, index=labels) # here keys will be provided lables
print("data_with_labels", data_with_labels)

data_using_numpy_array = pd.Series(data=arr, index=labels) # We can create series with numpy array
print("data_using_numpy_array", data_using_numpy_array)

data_using_dictionary = pd.Series(d) # the keys will be same as dictionary keys
print("data_using_dictionary", data_using_dictionary) 

any_data = pd.Series([print, sum, len]) # data points can also be python objects
print("any_data", any_data)

# performing operations on series
series1 = pd.Series([1,2,3], ['a', 'b', 'c'])
series2 = pd.Series([1,4,2], ['a', 'd', 'b'])
print("series1 + series2", series1 + series2) 
# for not found data it will return NaN in above example c and d will be NaN as it not present in one of series
# if we perform operations on series the integers will always get converted into floats