# Generator Explanation

# 1. Definition:
#    - Generators are special functions used to create iterators.
#    - Defined using the `yield` keyword instead of `return`.

# 2. How Generators Work:
#    a. `yield` Keyword:
#       - Used to produce a value from the generator.
#       - Saves the function's state and returns the yielded value to the caller.
#    b. Lazy Evaluation:
#       - Values are produced on demand.
#       - Does not store all values in memory, making it memory-efficient.
#    c. Iterator:
#       - Generator objects are iterators.
#       - Can be used in `for` loops or with the `next()` function.
#    d. State Preservation:
#       - When `next()` is called, execution resumes from where it left off, using the saved state.


# generator implementation

# Example 1: Simple Number Generator

def number_generator():
    for i in range(5):
        yield i

# Using the generator
gen = number_generator()

for num in gen:
    print(num)

print('-------------------------------------------')

# Example 2: Fibonacci Sequence Generator

def fibonacci_gen(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1
    
gen = fibonacci_gen(7)
print(gen)

for num in gen:
    print(num)

print('-------------------------------------------')


# Example 3: Generator with next()

def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(3)

print(next(gen))
print(next(gen))
print(next(gen))

print('-------------------------------------------')

# Summary

# Use yield to turn a function into a generator.
# Each yield pauses the function and saves its state.
# Generators are great for working with large data streams or infinite sequences.


# Class-Based Generator Example

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

gen = Counter(3)

print(next(gen))
print(next(gen))
print(next(gen))
