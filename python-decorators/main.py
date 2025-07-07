def my_decorator(func):
    """
    A basic decorator that adds behavior before and after function execution.
    
    Args:
        func: The function to be decorated
        
    Returns:
        wrapper: The enhanced function with added behavior
    """
    def wrapper():
        """
        Inner function that wraps the original function.
        This is what actually gets called when the decorated function is invoked.
        """
        # Execute code before the original function
        print("Before function call")
        
        # Call the original function
        func()
        
        # Execute code after the original function
        print("After function call")
    
    # Return the wrapper function (this replaces the original function)
    return wrapper

# The @ symbol applies the decorator to the function below
# This is equivalent to: say_hello = my_decorator(say_hello)
@my_decorator
def say_hello():
    """
    A simple function that prints a greeting.
    This function will be enhanced by my_decorator.
    """
    print("Hello!")

def timer_decorator(func):
    """
    A decorator that measures and prints the execution time of a function.
    
    Args:
        func: The function to be timed
        
    Returns:
        wrapper: Function with timing functionality added
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that handles functions with any number of arguments.
        
        Args:
            *args: Variable length argument list (positional arguments)
            **kwargs: Variable length keyword argument dictionary
            
        Returns:
            The result of the original function call
        """
        # Import time module for timing functionality
        import time
        
        # Record start time before function execution
        start = time.time()
        
        # Call original function with all its arguments and capture result
        # *args unpacks positional arguments, **kwargs unpacks keyword arguments
        result = func(*args, **kwargs)
        
        # Record end time after function execution
        end = time.time()
        
        # Calculate and display execution time
        print(f"Function took {end - start:.4f} seconds")
        
        # Return the original function's result
        return result
    
    # Return the enhanced wrapper function
    return wrapper

# Apply timer_decorator to slow_function
@timer_decorator
def slow_function(n):
    """
    A function that simulates slow execution by sleeping.
    
    Args:
        n (int/float): Number of seconds to sleep
        
    Returns:
        str: Message indicating how long the function slept
    """
    # Import time module for sleep functionality
    import time
    
    # Pause execution for n seconds
    time.sleep(n)
    
    # Return a message about the sleep duration
    return f"Slept for {n} seconds"

# Main execution block - only runs when script is executed directly
if __name__ == "__main__":
    # Call the decorated say_hello function
    # This will trigger: "Before function call" -> "Hello!" -> "After function call"
    say_hello()
    
    # Print empty line for better output formatting
    print()
    
    # Call the decorated slow_function with argument 1
    # This will time the execution and print the duration
    result = slow_function(1)
    
    # Print the return value from slow_function
    print(result)