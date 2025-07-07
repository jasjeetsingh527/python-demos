from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ["sisi", "bibi", "titi", "carla"]
print(list(map(lambda x: x.capitalize(), my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(lambda x: x > 50, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

print(reduce(lambda x, y: x + y, my_numbers + scores))  # Output: 456

# square my_numbers
print(list(map(lambda x: x**2, my_numbers)))

# sorting the list of tuples according to 2nd element
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(a, key=lambda x: x[1]))

# explain: the sorted() function sorts the list of tuples according to the second element of each tuple. The key

users = [
    {
        "id": 10,
        "name": "John",
    },
    {
        "id": 20,
        "name": "Jane",
    },
    {
        "id": 5,
        "name": "Jim",
    },
    {
        "id": 7,
        "name": "Jill",
    },
]

print(sorted(users, key=lambda x: x["id"]))
print(sorted(users, key=lambda x: x["name"]))
