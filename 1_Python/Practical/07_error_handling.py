# 1. Handling an error when dividing by zero

# If you try to divide by zero, Python raises a ZeroDivisionError. 
# Use try-except to catch it.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# 2. Handling multiple possible errors

# You can catch different types of errors separately, like invalid input (ValueError) 
# and division by zero (ZeroDivisionError).

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# 3. Catching all exceptions with a message

# Sometimes you want to catch any error that might happen and print the error message.

try:
    # Some risky code
    result = 10 / int("abc")
except Exception as e:
    print(f"An error occurred: {e}")

# 4. Running code only if no error occurs (else)

# Use the else block for code that runs only when no exception was raised.

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered {x}, which is valid.")

# 5. Code that always runs, even if there’s an error (finally)

# Use finally to run cleanup code that must run regardless of success or failure.

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except Exception as e:
    print(f"Error: {e}")
finally:
    print("This runs no matter what.")

# 6. Creating and raising a custom error

# You can define your own exception class for custom error handling.

class MyError(Exception):
    pass

try:
    raise MyError("This is a custom error!")
except MyError as e:
    print(e)
