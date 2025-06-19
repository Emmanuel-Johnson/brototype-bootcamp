#Flatten list

nested = [1, [2, [3, 4], 5], [6, 7], 8]

def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten(nested))