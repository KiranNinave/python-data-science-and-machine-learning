# map
def number(n):
    return n


seqence = [1, 2, 3, 4, 5]

result = map(number, seqence)

# another version

result = map(lambda n: n, seqence)

print("result", list(result))

filter_result = filter(lambda n: n % 2 == 0 if True else False, seqence)

print("filter_result", list(filter_result))

# tuple unpacking
tuple_list = [(1, 2), (3, 4)]
for a, b in tuple_list:
    print(a, b)
