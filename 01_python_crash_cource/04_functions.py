def my_function(name="default name"):
    """
    my_function will print name with hello message and return it
    """
    print("hello + " + name)
    return name


print(type(my_function), my_function)
my_function(name="kiran")
