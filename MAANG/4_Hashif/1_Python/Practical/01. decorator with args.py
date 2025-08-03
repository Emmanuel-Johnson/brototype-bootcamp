def repeat(num_times):
    """Decorator factory: repeats the function call num_times times."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result  # return result of last call
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Emmanuel")
