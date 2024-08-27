# Задание 5.

# Пишем функцию, в которой параметрами будут длины двух сторон треугольника - наша задача узнать третью. Важно - мы можем ввести два катета или катет и гипотенузу. Поэтому параметра у функции будет три - им всем мы задаем значение 0.

def orth_triangle(*, cathet1: float=0, cathet2: float=0, hypotenuse: float=0):

# Проверяем три условия:
# 1. Если катеты и гипотенузы не равны нулю - возвращаем None.
# 2. Если гипотенуза равна 0, то вычисляем ее с помощью теоремы Пифагора.
# 3. Если гипотенуза больше суммы катетов, то так можно вычислить один из катетов треугольника.
# 4. Если гипотенуза меньше суммы катетов - вычисление невозможно.

    if cathet1 !=0 and cathet2 !=0 and hypotenuse !=0:
        return None

    if hypotenuse == 0:
        return (cathet1**2 + cathet2**2) ** 0.5

    cat_sum = cathet1 + cathet2

    if hypotenuse > cat_sum:
        return (hypotenuse**2 - cat_sum**2) ** 0.5
    else :
        return None
    

print(orth_triangle(cathet1=3, hypotenuse=5))
    # 4.0
print(orth_triangle(cathet1=8, cathet2=15))
    # 17.0
print(orth_triangle(cathet2=9, hypotenuse=3))
    # None