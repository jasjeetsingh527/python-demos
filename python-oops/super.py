class User:
    """Base class representing a generic user with basic properties and methods."""
    
    def __init__(self, name, age):
        """Initialize a User instance with name, age, and empty books list.
        
        Args:
            name (str): The user's name
            age (int): The user's age
        """
        self.name = name      # Store the user's name as instance attribute
        self.age = age        # Store the user's age as instance attribute
        self.books = []       # Initialize empty list to store user's books

    def sign_in(self):
        """Method to handle user sign-in process."""
        print("User sign in.")  # Print sign-in message


class Archer(User):
    """Archer class that inherits from User, representing a specialized user type."""

    def __init__(self, name, age, num_arrows):
        """Initialize an Archer instance with inherited User properties plus arrows.
        
        Args:
            name (str): The archer's name (passed to parent class)
            age (int): The archer's age (passed to parent class)
            num_arrows (int): Number of arrows the archer has (currently unused)
        """
        # Call parent class constructor to initialize name, age, and books
        super().__init__(name, age)
        # Note: Bug here - num_arrows parameter is ignored, always set to 0
        self.num_arrows = 0

    def attack(self):
        """Method specific to Archer class to perform attack action."""
        # Print attack message using inherited name/age and archer-specific num_arrows
        print(f"{self.name}, {self.age}, attack with {self.num_arrows} arrows.")


# Create an Archer instance with name "John", age 30, and 50 arrows
archer = Archer("John", 30, 50)

# Call inherited sign_in method (returns None, so prints None)
print(archer.sign_in())

# Call archer-specific attack method (returns None, so prints None)
print(archer.attack())
