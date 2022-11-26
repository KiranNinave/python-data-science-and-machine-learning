# number
# python has 3 numeric data types, i.e int, float, complex
integer_number = 1
print(type(integer_number), integer_number)  # output: <class 'int'> 1

float_number = 1.1
print(type(float_number), float_number)  # output: <class 'float'> 1.1

complex_number = 100+1j
print(type(complex_number), complex_number)
# output: <class 'complex'> (100+1j)


# string
string = "my string"
print(type(string), string)

# string formatting
print('variable {one} , variable {two}'.format(one=1, two=2))

# string slicing
print(string[0], string[3:9])


# sequence types
# list
my_list = [1, 2, 3]
print(type(my_list), my_list)  # output: <class 'list'> [1, 2, 3]

# adding
my_list.append(4)

# access
print(my_list[0], my_list[0:3])  # output: 1 [1, 2, 3]

# tuple
# the only diffrence between list and tuple is that tuple is not mutable
my_tuple = (1, 2, 3)
print(type(my_tuple), my_tuple)  # output: <class 'tuple'> (1, 2, 3)


# mapping data types
# dictionary (key value pair like hashmap)
my_dictionary = {"key1": "string key", "key2": 123, 2: 2}
# output: <class 'dict'> {'key1': 'string key', 'key2': 123, 2: 2}
print(type(my_dictionary), my_dictionary)

# access
print(my_dictionary["key1"], my_dictionary[2])  # output: string key 2


# sets
# A set is a collection which is unordered, unchangeable*, and unindexed.
# set cant have duplicate values
my_set = {"1", "3", "2"}
my_set.add("4")
my_set.add("4")
print(type(my_set), my_set)

# frozenset
# the only diffrence between set and frozenset is that frozenset is unchanble its locked
my_frozen_set = frozenset(my_set)
print(type(my_frozen_set), my_frozen_set)
