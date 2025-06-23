# fundamental Data types in Python
# int
print(2 + 4)
print(type(2 + 4))

# float
print(2.5 + 4.5)
print(type(2.5 + 4.5))

# Why there is float and int?
# In Python, `int` is used for whole numbers, while `float` is used for
# numbers with decimal points. The distinction allows for more precise calculations
# when dealing with fractions or real-world measurements. For example, `2` is an `int` and `2.5` is a `float`. When you perform arithmetic operations, Python automatically
# converts `int` to `float` if necessary to maintain precision. This is why you
# can add an `int` and a `float` together, and the result will be a `float`.
# A float number requires more memory than an int number.

# Double **
print(2**3)  # 2 raised to the power of 3
print(type(2**3))

# Double //
print(5 // 2)  # Floor division, result is 2

# modulus %
print(5 % 2)  # Remainder of division, result is 1

# bin() - binary representation
print(bin(5))  # Output: '0b101'
print(int("0b101", 2))  # Convert binary string to int, Output: 5
