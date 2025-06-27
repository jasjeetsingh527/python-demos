# Dictionary is a collection of key-value pairs. It is an also known as an associative array or hash map in other programming languages. It is a mutable data type in Python, meaning it can be modified after it is created.

# example of a dictionary
dict1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "History"],
    "address": {"street": "123 Main St", "zip": "10001"},
}
print(dict1)
print(dict1["name"])  # prints Alice

list_of_dict = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]
print(list_of_dict[1]["name"])  # prints Bob

# accessing dictionary values
print(dict1["age"])  # prints 30
print(dict1["courses"])  # prints ['Math', 'Science', 'History']
print(dict1["address"]["street"])  # prints 123 Main St

# return list of keys
print(
    dict1.keys()
)  # prints dict_keys(['name', 'age', 'city', 'is_student', 'courses', 'address'])

# return list of values or items
print(
    dict1.values()
)  # prints dict_values(['Alice', 30, 'New York', False, ['Math', 'Science', 'History'], {'street': '123 Main St', 'zip': '10001'}])

# get method
print(dict1.get("name"))  # prints Alice
print(dict1.get("country"))  # prints None, key not found
print(dict1.get("country", "USA"))  # prints USA, default value if key
