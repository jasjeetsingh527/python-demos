# Tuple are immutable sequences in Python, used to store multiple items in a single variable.
# Tuples are defined by enclosing the items in parentheses `()`, separated by commas.

# Example of a tuple
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)  # prints (1, 2, 3, 4, 5)

# Mixed data types in a tuple
tuple2 = (1, "apple", 3.14, True)
print(tuple2)  # prints (1, 'apple', 3.14, True)

# Accessing tuple elements
print(tuple1[0])  # prints 1, first element
print(tuple2[1])  # prints apple, second element

# Slicing a tuple
print(tuple1[1:4])  # prints (2, 3, 4
print(tuple2[:2])  # prints (1, 'apple')
print(tuple2[2:])  # prints (3.14, True)
# Tuple with a single element (note the comma)
tuple3 = (42,)
print(tuple3)  # prints (42)

# methods on tuples
# 1. Count: returns the number of occurrences of a value
count_of_1 = tuple1.count(1)  # counts how many times 1
print(count_of_1)  # prints 1, since 1 appears once in tuple1

# 2. Index: returns the index of the first occurrence of a value
index_of_3 = tuple1.index(3)  # finds the index of 3
print(index_of_3)  # prints 2, since 3 is at index 2 in tuple1

# Safely checking for a value in a tuple
index_of_6 = tuple1.index(6) if 6 in tuple1 else None  # safely checks for 6 in tuple1
print(index_of_6)  # prints None, since 6 is not in tuple1
