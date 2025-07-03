# => OOPS - Object-Oriented Programming demonstration
# This file shows the basics of classes, objects, and different types of methods


# CLASS DEFINITION: Blueprint for creating Person objects
class Person:
    """
    Person class represents a person with name and age.
    Demonstrates instance methods, class methods, and static methods.
    """

    # CONSTRUCTOR METHOD (__init__): Special method that runs when creating new objects
    def __init__(self, name, age):
        """
        Initialize a new Person object.

        Parameters:
        name (str): Person's name
        age (int): Person's age
        """
        # 'self' refers to the specific instance being created
        # INSTANCE VARIABLES: Each Person object gets its own copy
        self.name = name  # Store person's name (unique to this object)
        self.age = age  # Store person's age (unique to this object)

    # INSTANCE METHOD: Works with specific object data (needs 'self')
    def greet(self):
        """
        Print a greeting message using this person's data.
        Instance methods can access self.name, self.age, etc.
        """
        # f-string formatting: {} allows inserting variables into strings
        # Access instance variables using self.variable_name
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # CLASS METHOD: Alternative constructor, works with the class itself
    @classmethod  # Decorator that marks this as a class method
    def from_string(cls, string):
        """
        Create a Person object from a comma-separated string.

        Parameters:
        cls: Reference to the class itself (Person)
        string (str): Format "name,age" like "Bob,25"

        Returns:
        Person: New Person object created from the string
        """
        # Split the string by comma to separate name and age
        name, age = string.split(",")
        # cls refers to the Person class, create new instance
        # int(age) converts age string to integer
        return cls(name, int(age))

    # STATIC METHOD: Utility function, doesn't need class or instance data
    @staticmethod  # Decorator that marks this as a static method
    def is_adult(age):
        """
        Check if given age represents an adult.

        Parameters:
        age (int): Age to check

        Returns:
        bool: True if age > 18, False otherwise
        """
        # Simple comparison, returns True or False
        return age > 18


# OBJECT INSTANTIATION: Creating objects from the class
print("=== Creating Person objects ===")

# Create first Person object by calling Person() constructor
# This runs __init__ method with "Alice" and 30 as arguments
Person1 = Person("Alice", 30)

# Call the greet method on Person1 object
# This will print: "Hello, my name is Alice and I am 30 years old."
Person1.greet()

print("\n=== Using class method and static method ===")

# CLASS METHOD EXAMPLE: Create Person from string using alternative constructor
# Call class method directly on the Person class (not on an instance)
person = Person.from_string("Bob, 25")

# Access instance variables of the newly created person object
print(f"Name from string: {person.name}")  # Prints: Bob
print(f"Age from string: {person.age}")  # Prints: 25

# STATIC METHOD EXAMPLE: Check if age represents an adult
# Call static method directly on the Person class
# This returns False because 16 is not > 18
print(f"Is 16 an adult? {Person.is_adult(16)}")  # Prints: False
