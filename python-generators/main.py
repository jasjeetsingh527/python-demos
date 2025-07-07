"""
Python Generators - Memory-efficient iteration using yield
"""


def number_generator(n):
    """
    Generator function that yields numbers from 0 to n-1.

    Args:
        n (int): Upper limit (exclusive)

    Yields:
        int: Sequential numbers from 0 to n-1
    """
    i = 0
    while i < n:
        yield i  # yield pauses function, returns value, resumes on next call
        i += 1


def fibonacci_generator(limit):
    """
    Generator for Fibonacci sequence up to limit.

    Args:
        limit (int): Maximum value to generate

    Yields:
        int: Next Fibonacci number
    """
    a, b = 0, 1
    while a < limit:
        yield a  # Return current value and pause
        a, b = b, a + b  # Calculate next values


# Usage examples
if __name__ == "__main__":
    # Generator creates iterator object, doesn't execute immediately
    gen = number_generator(5)
    print(f"Generator object: {gen}")

    # Iterate through generator values
    print("Numbers:")
    for num in gen:
        print(num)  # Prints 0, 1, 2, 3, 4

    # Generator expression (like list comprehension but lazy)
    squares = (x**2 for x in range(5))
    print(f"Squares: {list(squares)}")  # [0, 1, 4, 9, 16]

    # Fibonacci example
    print("Fibonacci sequence:")
    for fib in fibonacci_generator(20):
        print(fib, end=" ")  # 0 1 1 2 3 5 8 13
