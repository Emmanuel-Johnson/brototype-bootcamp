def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
    
gen = fibonacci()

print(gen)
    
print(next(gen))
print(next(gen))
print(next(gen))

# or 

print("-----------------------------------------------")

gen = fibonacci()
for _ in range(5):
    print(next(gen))


# or

print("-----------------------------------------------")

for num in fibonacci():
    print(num)
    if num > 10:   # stop manually to avoid infinite loop
        break
