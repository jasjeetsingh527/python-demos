# lists are arrays that can hold multiple values
# they can hold different data types
# they are mutable, meaning you can change them after creation
list1 = [1, 2, 3, 4, 5]
list2 = ["apple", "banana", "cherry"]
mixed_list = [1, "apple", 3.14, True]

# slicing
# list2[start:end:step]
print(list2[1:3])  # prints ['banana', 'cherry']

list2[0] = "orange"  # changing the first element
print(list2)  # prints ['orange', 'banana', 'cherry']

new_list2 = list2
copy_list2 = list2[:]
list2[0] = "kiwi"  # changing the first element of list2
print(new_list2)  # prints ['kiwi', 'banana', 'cherry']

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # prints 6, accessing the second row and third column

# methods on lists
# 1. Append
list1.append(6)  # adds 6 to the end of list1
print(list1)  # prints [1, 2, 3, 4, 5, 6]

# 2. Insert
list1.insert(0, 0)  # inserts 0 at the beginning of list1
print(list1)  # prints [0, 1, 2, 3, 4, 5, 6]

# 3. Extend
list1.extend([7, 8, 9])  # adds multiple elements to the end of list1
print(list1)  # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4. Pop: removes and returns the last element
last_element = list1.pop()  # removes and returns the last element
print(last_element)  # prints 9
print(list1)  # prints [0, 1, 2, 3, 4, 5, 6, 7, 8]

pop = list1.pop(0)  # removes and returns the first element
print(pop)  # prints 0
print(list1)  # prints [1, 2, 3, 4, 5, 6, 7, 8]

# 5. Remove: removes the first occurrence of a value
list1.remove(5)  # removes the first occurrence of 5
print(list1)  # prints [1, 2, 3, 4, 6, 7, 8]

# 6. Clear: removes all elements from the list
list1.clear()  # clears the list
print(list1)  # prints []


# 7. Index: returns the index of the first occurrence of a value
list2 = ["apple", "banana", "cherry"]
index_of_banana = list2.index("banana")  # finds the index of "banana"
print(index_of_banana)  # prints 1

index_of_peach = (
    list2.index("peach") if "peach" in list2 else -1
)  # safely checks for "peach" in the list in the list
print(index_of_peach)  # prints -1, since "peach" is not

# 8. Count: returns the number of occurrences of a value
count_of_apple = list2.count("apple")  # counts occurrences of "apple"
print(count_of_apple)  # prints 1

# 9. Sort: sorts the list in ascending order
list2.sort()  # sorts the list in place
print(list2)  # prints ['apple', 'banana', 'cherry']

sorted_list = sorted(list2)  # returns a new sorted list without modifying the original
print(sorted_list)  # still prints ['apple', 'banana', 'cherry']
# 10. Reverse: reverses the order of the list
list2.reverse()  # reverses the list in place
print(list2)  # prints ['cherry', 'banana', 'apple']

list2.sort(reverse=True)  # sorts the list in descending order
print(list2)  # prints ['cherry', 'banana', 'apple']

# 11. Copy: creates a shallow copy of the list
list3 = list2.copy()  # creates a shallow copy of list2
print(list3)  # prints ['cherry', 'banana', 'apple']


# 12. Join: joins elements of a list into a string
joined_string = ", ".join(list2)  # joins elements with a comma and space
print(joined_string)  # prints 'cherry, banana, apple'


# 13. Range: creates a list of numbers
range_list = list(range(10))  # creates a list of numbers from 0 to 9
print(range_list)  # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# list unpacking
a, b, c = [1, 2, 3]  # unpacking the first three elements
print(a, b, c)  # prints 1 2 3
# unpacking with asterisk
d, *e, f = [4, 5, 6, 7]  # unpacking the first element and the rest into a list
print(d, e, f)  # prints 4 [5, 6] 7
