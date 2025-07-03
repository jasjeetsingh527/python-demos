# Container class that manages a collection of pet animals
class Pets:
    # Class variable - shared by all instances (potential issue: mutable default)
    animals = []

    # Constructor - initializes each instance with its own list of animals
    def __init__(self, animals):
        # Instance variable - each Pets object gets its own animals list
        self.animals = animals

    # Method to make all pets walk - demonstrates polymorphism
    def walk(self):
        # Iterate through each animal in the collection
        for animal in self.animals:
            # Call each animal's walk() method and print the result
            # This works because all animals have a walk() method
            print(animal.walk())


# Base Cat class - parent class for all cat types
class Cat:
    # Class variable - shared characteristic of all cats
    is_lazy = True

    # Constructor - initializes each cat with name and age
    def __init__(self, name, age):
        # Instance variables - unique to each cat object
        self.name = name
        self.age = age

    # Method that returns a string describing the cat's walking behavior
    def walk(self):
        # Uses f-string formatting to include the cat's name
        return f"{self.name} is just walking around"


# Simon class inherits from Cat - demonstrates inheritance
class Simon(Cat):
    # Additional method specific to Simon - extends base Cat functionality
    def sing(self, sounds):
        # Simply returns the sounds parameter as a string
        return f"{sounds}"


# Sally class also inherits from Cat - same structure as Simon
class Sally(Cat):
    # Same sing method as Simon - could be refactored to base class
    def sing(self, sounds):
        return f"{sounds}"


# 1 Add another Cat - Tommy class following the same inheritance pattern
class Tommy(Cat):
    # Identical sing method - demonstrates code duplication that could be improved
    def sing(self, sounds):
        return f"{sounds}"


# 2 Create a list of all of the pets (create 3 cat instances from the above)
# Instantiate each cat class with name and age parameters
simon = Simon("Simon", 2)  # Creates a Simon object with name "Simon" and age 2
sally = Sally("Sally", 4)  # Creates a Sally object with name "Sally" and age 4
tommy = Tommy("Tommy", 6)  # Creates a Tommy object with name "Tommy" and age 6

# Create an empty list to store all cat instances
my_cats = []
# Add each cat instance to the list
my_cats.append(simon)  # Add Simon to the collection
my_cats.append(sally)  # Add Sally to the collection
my_cats.append(tommy)  # Add Tommy to the collection

# 3 Instantiate the Pet class with all your cats use variable my_pets
# Create a Pets object that manages all the cats in the my_cats list
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance
# Call the walk method which will iterate through all cats and print their walking behavior
my_pets.walk()
# This will output:
# Simon is just walking around
# Sally is just walking around
# Tommy is just walking around
