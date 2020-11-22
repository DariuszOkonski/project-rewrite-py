def min(x, y):
    if x < y:
        return x
    return y


def max(values_list):
    max = values_list[0]
    for item in values_list:
        if item > max:
            max = item
    return max


def len(values_list):
    counter = 0
    for i in values_list:
        counter += 1
    return counter


def multiply(x, y):
    counter = 0
    multiply = 0

    while counter < y:
        multiply += x
        counter += 1
    
    return multiply


def pow(x, y):
    counter = 0
    multiply = 1

    while counter < y:
        multiply *= x
        counter += 1
    
    return multiply


def divmod(x, y):
    result = x / y
    res_first = int(result)
    res_seond = x - (y * res_first)
    return (res_first, res_seond)
    

print(divmod(10,3))
print(divmod(11,3))
print(divmod(12,3))
