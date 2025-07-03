# Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP)
# that bundles data and the methods that operate on that data within a single unit or object.

# Key aspects of encapsulation:
# 1. Data Hiding: Making data private using access modifiers (private, protected, public)
# 2. Data Protection: Preventing direct access to internal implementation details
# 3. Access Control: Providing controlled access through getter/setter methods
# 4. Bundling: Keeping related data and methods together in a class


# Example of encapsulation:
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private variable with double underscore

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
