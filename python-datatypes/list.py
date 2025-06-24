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
