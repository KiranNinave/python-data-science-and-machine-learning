# for loop
# for loop allow us to interate in sequence
my_seq = [1, 2, 3, 4, 5]
squares = []
for i in my_seq:
    squares.append(i ** 2)
print("squares", squares)

# list comprehension
squares = {i ** 2 for i in my_seq}
print("squares with new syntax", squares)


# while loop
i = 1
while (i <= 5):
    print('i is {}'.format(i))
    i += 1
