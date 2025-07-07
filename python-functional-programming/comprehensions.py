# list, set, dictionary

string_list = [char for char in "Hello World!"]
print(string_list)

range_list = [num for num in range(100)]
print(range_list)

even_only = [num for num in range(100) if num % 2 == 0]
print(even_only)


# => Sets

string_set = {char for char in "Hello World!"}
print(string_set)

range_set = {num for num in range(100)}
print(range_set)

even_only_set = {num for num in range(100) if num % 2 == 0}
print(even_only_set)


some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
duplicates = list(set(i for i in some_list if some_list.count(i) > 1))

print(f"Duplicate list: {duplicates}")
