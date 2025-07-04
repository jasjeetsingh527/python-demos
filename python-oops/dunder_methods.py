# Demonstrating common Python dunder (double underscore) methods


class DunderDemo:
    def __init__(self, name, value):
        """Constructor method"""
        self.name = name
        self.value = value

    def __str__(self):
        """String representation for end users"""
        return f"{self.name} with value: {self.value}"

    def __repr__(self):
        """String representation for developers"""
        return f"DunderDemo(name='{self.name}', value={self.value})"

    def __len__(self):
        """Returns length of name"""
        return len(self.name)

    def __eq__(self, other):
        """Equality comparison"""
        if not isinstance(other, DunderDemo):
            return False
        return self.name == other.name and self.value == other.value

    def __lt__(self, other):
        """Less than comparison"""
        if not isinstance(other, DunderDemo):
            return NotImplemented
        return self.value < other.value

    def __add__(self, other):
        """Addition operator"""
        if isinstance(other, DunderDemo):
            return DunderDemo(f"{self.name}+{other.name}", self.value + other.value)
        return DunderDemo(self.name, self.value + other)

    def __getitem__(self, key):
        """Index/key access"""
        if key == "name":
            return self.name
        elif key == "value":
            return self.value
        raise KeyError(f"'{key}' not found")

    def __call__(self):
        """Makes object callable"""
        return f"Called {self.name} with value {self.value}"

    def __enter__(self):
        """Context manager entry"""
        print(f"Entering context for {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Context manager exit"""
        print(f"Exiting context for {self.name}")


# Example usage:
if __name__ == "__main__":
    obj1 = DunderDemo("First", 10)
    obj2 = DunderDemo("Second", 20)

    # __str__ and __repr__
    print(str(obj1))  # First with value: 10
    print(repr(obj1))  # DunderDemo(name='First', value=10)

    # __len__
    print(len(obj1))  # 5 (length of "First")

    # __eq__
    print(obj1 == obj2)  # False

    # __lt__
    print(obj1 < obj2)  # True

    # __add__
    obj3 = obj1 + obj2
    print(obj3.name)  # First+Second
    print(obj3.value)  # 30

    # __getitem__
    print(obj1["name"])  # First
    print(obj1["value"])  # 10

    # __call__
    print(obj1())  # Called First with value 10

    # __enter__ and __exit__
    with obj1:
        print("Inside context manager")
