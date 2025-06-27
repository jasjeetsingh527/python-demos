# Set are unordered collections of unique elements.
# They are defined by enclosing the elements in curly braces `{}` or using the `set()`
# constructor. Sets are useful for membership testing and eliminating duplicate entries.

# Example of a set
set1 = {1, 2, 3, 4, 5}
print(set1)  # prints {1, 2, 3, 4, 5}
# Mixed data types in a set
set2 = {1, "apple", 3.14, True}
print(set2)  # prints {1, 3.14, 'apple'}

# Exersces

my_list = [1, 2, 3, 4, 5, 1, 2, 3]
my_set = set(my_list)
print(my_set)  # prints {1, 2, 3, 4, 5}, duplicates are removed

# Accessing elements in a set
# Sets do not support indexing or slicing since they are unordered.
# However, you can iterate through a set.
for item in set1:
    print(item)  # prints each item in set1


# methods on sets
# 1. Difference: returns a new set with elements in the first set but not in the second
set3 = {1, 2, 3}
set4 = {3, 4, 5}
difference = set3.difference(set4)  # elements in set3 but not in set4
print(difference)  # prints {1, 2}

# 2. Discard: removes an element from the set if it exists, does nothing if it doesn't
set3.discard(2)  # removes 2 from set3
print(set3)  # prints {1, 3}
set3.discard(5)  # does nothing, since 5 is not in set3

# 3. Intersection: returns a new set with elements common to both sets
intersection = set3.intersection(set4)  # common elements in set3 and set4
print(intersection)  # prints {3}

# 4. Is Disjoint: checks if two sets have no elements in common
is_disjoint = set3.isdisjoint(set4)  # checks if set3 and
# set4 have no common elements
print(is_disjoint)  # prints False, since they have 3 in common

# 5. Is Subset: checks if one set is a subset of another
is_subset = set3.issubset(set4)  # checks if set3 is
# a subset of set4
print(is_subset)  # prints False, since set3 is not a subset of set4

# 6. Is Superset: checks if one set is a superset of another
is_superset = set4.issuperset(set3)  # checks if set4
# is a superset of set3
print(is_superset)  # prints True, since set4 contains all elements of set3
