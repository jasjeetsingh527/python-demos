# Given the below class:
# This is a blueprint for creating cat objects
class Cat:
    # All cats are mammals - this is shared by every cat
    species = "mammal"

    # This runs when we create a new cat - like filling out a form
    def __init__(self, name, age):
        # Each cat gets its own name
        self.name = name
        # Each cat gets its own age
        self.age = age


# 1 Instantiate the Cat object with 3 cats
# Make 3 different cats with different names and ages
cat1 = Cat("cat1", 2)  # First cat is 2 years old
cat2 = Cat("cat2", 3)  # Second cat is 3 years old
cat3 = Cat("cat3", 4)  # Third cat is 4 years old


# 2 Create a function that finds the oldest cat
# This function can take any number of ages and find the biggest one
def oldest_cat(*args):
    # max() picks the biggest number from all the numbers given
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# Get the ages of all 3 cats, find the oldest, and print the result
# This will print: "The oldest cat is 4 years old."
print(f"The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")
