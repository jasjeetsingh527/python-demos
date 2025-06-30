is_old = False
have_license = False

if is_old and have_license:
    print("You can drive the car.")
elif is_old and not have_license:
    print("You are old enough but you don't have a license.")
elif not is_old and have_license:
    print("You have a license but you are not old enough.")
else:
    print("You are neither old enough nor do you have a license.")
print("End of the program.")

# Truthy and Falsy values
# In Python, the following values are considered False:
# - None
# - False
# - 0 (zero of any numeric type)
# - Empty sequences and collections (e.g., '', [], {}, set(), ())
# All other values are considered True.

# Example of truthy and falsy values
value = None
if value:
    print("This is a truthy value.")
else:
    print("This is a falsy value.")

# Ternary operator
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Short circuit evaluation
if is_old or have_license:
    print("You can drive the car.")
else:
    print("You cannot drive the car.")
