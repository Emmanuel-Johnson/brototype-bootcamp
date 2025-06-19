# Dict comprehension

original_dict = {'a': 2, 'b': 3, 'c': 4}

# Square the values
squared_dict = {k: v ** 2 for k, v in original_dict.items()}

print(squared_dict)
