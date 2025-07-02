# decorator to convert string returns to lowercase

def to_lowercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.lower()
        return result
    return wrapper


@to_lowercase_decorator
def greet():
    return "HELLO WORLD"

print(greet()) 


""" 
def to_lowercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.lower()
        return result
    return wrapper



def greet(message):
    return message

greet = to_lowercase_decorator(greet)

print(greet("HELLO WORLD"))  
"""