# Generator Implementation

# A generator in Python is a function that returns an iterator and allows you to 
# iterate over a potentially large sequence of values one at a time using the `yield` keyword. 
# Unlike regular functions that use `return`, a generator can pause its execution and resume later, saving memory.

# Basic Generator Example
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Usage
counter = count_up_to(5)
for num in counter:
    print(num)
# Output:
# 1
# 2
# 3
# 4
# 5

# Generator Expression (One-liner)
squares = (x * x for x in range(10))
for s in squares:
    print(s)
