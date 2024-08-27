# Задание 1.

# Создаем функцию double_fact с параметром n. Внутри функции пишем условие - если число равно 0 или 1 - функция возвращает значение 1. В любом другом случае функция возвращает 

def double_fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * double_fact(n-2)
    
x = double_fact(6)
y = double_fact(5)
z = double_fact(2)
k = double_fact(4)
print(x)
print(y)
print(z)
print(k)

# Вход: 6
# Выход: 48

# Вход: 5
# Выход: 15

# Вход: 2
# Выход: 2

# Вход: 4
# Выход: 8