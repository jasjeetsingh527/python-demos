"""Datatypes: Strings"""

username = "john_doe"
password = "secure_password"
long_string = """This is a very long 
string that might need to be 
truncated or processed 
in some way."""

print("Username:", username)
print("Password:", password)
print("Long String:", long_string)

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation
print("Full Name:", full_name)

# String Concatenations
greeting = "Hello, " + first_name + " " + last_name + "!"
print(greeting)


# Escape Sequences
escaped_string = (
    'This is a string with a newline\nand a tab\tand a backslash\\ with "some quotes".'
)
print("Escaped String:", escaped_string)

# Formatted Strings
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted String:", formatted_string)


# string indexing
sample_string = "Hello, World!"
# sample_string[start:end:step]
print("First character:", sample_string[0])  # H
print("Last character:", sample_string[-1])  # !

print("Substring (0-5):", sample_string[0:5])  # Hello
print("Substring (7-):", sample_string[7:])  # World!

print("Substring stepover:", sample_string[0:7:2])  # World

print("Reversed String:", sample_string[::-1])  # !dlroW ,olleH

# immutibility
# Strings are immutable, meaning they cannot be changed after creation.
# You can create a new string based on an existing one, but you cannot modify the original string
