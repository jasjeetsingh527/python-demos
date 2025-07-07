"""Functional Programming in Python

This module demonstrates functional programming concepts:

1. Pure Functions: Functions that always return the same output for the same input
   and have no side effects (don't modify external state)

2. Higher-Order Functions: Functions that take other functions as arguments
   or return functions (map, filter, reduce, zip)

3. Lambda Expressions: Anonymous functions for simple operations
   Syntax: lambda arguments: expression

4. Immutability: Data structures that cannot be changed after creation

5. Function Composition: Combining simple functions to build complex operations

Key Benefits:
- More predictable code (no side effects)
- Easier testing and debugging
- Better parallelization
- Cleaner, more readable code
"""

from functools import reduce

# Core functional programming built-ins:
# map(function, iterable) - applies function to each item
# filter(function, iterable) - filters items based on condition
# reduce(function, iterable) - reduces iterable to single value

# Lambda syntax:
# map(lambda item_from_list: operation_on_item_from_list, list)
# filter(lambda item_from_list: condition_on_item_from_list, list)
# reduce(lambda x, y: operation_on_x_and_y, list)


# Traditional imperative approach
def multiply_by_two(li):
    """Multiply each element by 2 using imperative style."""
    new_list = []
    for i in li:
        new_list.append(i * 2)
    return new_list


# Functional programming approaches
def multiply_by_two_functional(li):
    """Multiply each element by 2 using map and lambda."""
    return list(map(lambda x: x * 2, li))


def filter_even_numbers(li):
    """Filter only even numbers using filter and lambda."""
    return list(filter(lambda x: x % 2 == 0, li))


def sum_all_numbers(li):
    """Sum all numbers using reduce and lambda."""
    return reduce(lambda x, y: x + y, li)


def zip_lists(li1, li2):
    """Combine two lists into a list of tuples using zip."""
    return list(zip(li1, li2))


# Higher-order function example
def apply_operation(li, operation):
    """Apply any operation to each element in the list."""
    return list(map(operation, li))


# Demo
data = [1, 2, 3, 4, 5, 6]
data2 = [10, 20, 30]
print(f"Original: {data}")
print(f"Doubled (imperative): {multiply_by_two(data)}")
print(f"Doubled (functional): {multiply_by_two_functional(data)}")
print(f"Even numbers: {filter_even_numbers(data)}")
print(f"Sum: {sum_all_numbers(data)}")
print(f"Zipped: {zip_lists(data, data2)}")  # only returns the first n elements
print(f"Squared: {apply_operation(data, lambda x: x**2)}")
