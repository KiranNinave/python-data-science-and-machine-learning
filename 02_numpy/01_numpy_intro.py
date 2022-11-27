# numpy is linear algebra library for python
# numpy is incredibly fast as it has binding to c library
# numpy arrays have two types vectors (1d array) and metrices (2d array)

import numpy as np

my_list = [1, 2, 3]

arr = np.array(my_list)
print(type(arr), arr)

arrange_array = np.arange(0, 10)
print("arrange_array", arrange_array)

zero_array = np.zeros((3,3))
print("zero_array", zero_array)

ones_array = np.ones(3)
print("ones_array", ones_array)

evenly_spaced_points = np.linspace(0, 5, 10)
print("evenly_spaced_points", evenly_spaced_points)

identity_metrix = np.eye(3)
print("identity_metrix", identity_metrix)

random_array = np.random.rand(5)
print("random_array", random_array)

random_neg_array = np.random.randn(5)
print("random_neg_array", random_neg_array)

random_int_array = np.random.randint(1, 100, 10)
print("random_int_array", random_int_array)

reshape_array = random_int_array.reshape(2,5)
print("reshape_array", reshape_array)

max_array = random_int_array.max()
print("max_array", max_array)

min_array = random_int_array.min()
print("min_array", min_array)

#indexing
print("indexing", random_int_array[2:5])

bool_array = random_int_array < 50
print("bool_array", bool_array)

conditional_array = random_int_array[bool_array]
print("conditional_array", conditional_array, "or", random_int_array[random_int_array < 50])