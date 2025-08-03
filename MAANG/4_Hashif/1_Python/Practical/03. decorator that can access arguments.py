def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Function `{func.__name__}` called with:")
        print(f"  Positional args: {args}")
        print(f"  Keyword args: {kwargs}")
        return func(*args, **kwargs)  # run the actual function
    return wrapper

@log_arguments
def greet(name, age=None):
    print(f"Hello {name}, age: {age}")

# Example usage
greet("Emmanuel", age=21)
