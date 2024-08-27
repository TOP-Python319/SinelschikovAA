# Задание 2.

def flatten(l:list):
    if isinstance(l, int):
        return [l]
    elif len(l) == 1 :
        return flatten(l[0])
    else :
        return flatten(l[0]) + flatten(l[1:])

print(flatten([1, [2, 3, [4]], 5])) 
print(flatten([1, [2, 3], [[2], 5], 6])) 
print(flatten([[[[9]]], [1, 2], [[8]]]))