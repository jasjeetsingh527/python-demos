# Inheritance: Inheritance allows a child class to inherit properties and methods from a parent class
# This promotes code reusability and establishes an "is-a" relationship


# Parent class (Base class) - defines common behavior for all users
class User:
    # Method that all users can perform - will be inherited by child classes
    def sign_in(self):
        print("User signed in")
        return True  # Returns boolean to indicate successful sign-in


# Child class (Derived class) - inherits from User class
# Wizard "is-a" User, so it gets all User methods plus its own specific methods
class Wizard(User):  # (User) indicates inheritance from User class
    # Constructor to initialize wizard-specific attributes
    def __init__(self, name, power):
        self.name = name  # Instance variable to store wizard's name
        self.power = power  # Instance variable to store wizard's power level

    # Method specific to Wizard class - defines how wizards attack
    def attack(self):
        print(f"attacking with power of {self.power}")


# Another child class inheriting from User
# Archer "is-a" User, so it also gets all User methods plus its own specific methods
class Archer(User):  # (User) indicates inheritance from User class
    # Constructor to initialize archer-specific attributes
    def __init__(self, name, arrows):
        self.name = name  # Instance variable to store archer's name
        self.arrows = arrows  # Instance variable to store number of arrows

    # Method specific to Archer class - defines how archers attack
    def attack(self):
        print(f"attacking with no of {self.arrows}")


# Creating instances and demonstrating inheritance
# Create a Wizard object with name "John" and power 400
wizard1 = Wizard("John", 400)
wizard1.sign_in()  # Calls inherited method from User class
wizard1.attack()  # Calls Wizard's own attack method

# Create an Archer object with name "Alice" and 800 arrows
archer1 = Archer("Alice", 800)
archer1.sign_in()  # Calls inherited method from User class
archer1.attack()  # Calls Archer's own attack method
