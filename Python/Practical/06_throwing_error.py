# throwing error

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!") 
    return a / b

try:
    result = divide(10, 0)
    print(result)
except ValueError as e:
    print(f"Error caught: {e}")
