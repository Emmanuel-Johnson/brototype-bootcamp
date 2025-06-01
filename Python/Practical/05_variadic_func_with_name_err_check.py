# variadic function that throws error if a kwarg of name 'err' is present

def func(*args, **kwargs):
    if 'err' in kwargs:
        raise ValueError("Keyword argument 'err' is not allowed")
    print("Args:", args)
    print("Kwargs:", kwargs)


func(1, 2, a=3)         
func(x=10)              
func(err="something")    


# All positional arguments (like 1, 2, 3, 4) go into *args as a tuple: (1, 2, 3, 4)

# All keyword arguments (like a=2) go into **kwargs as a dictionary: {'a': 2}

