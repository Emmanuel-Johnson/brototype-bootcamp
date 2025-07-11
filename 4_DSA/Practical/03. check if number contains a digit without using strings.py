# check if number contains a digit without using strings

number, digit = 1234890, 7

def my_func(number, digit):
    while number:                          # Loop until number becomes 0
        last_number = number % 10          # Extract last digit
        if last_number == digit:           # Compare with given digit
            return True
        number //= 10                      # Remove last digit
    return False

print(my_func(number, digit))              # Call Function and print result
