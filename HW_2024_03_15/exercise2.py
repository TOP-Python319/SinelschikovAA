# Задание  2.

fruits = []

while True:
    fruit = input()
    if fruit:
        fruits.append(fruit)
    else:
        break

if len(fruits) == 1:
    print(fruits[0])
else:
    formatted_string = ", ".join(fruits[:-1]) + " и " + fruits[-1]
    print(formatted_string)

# Пример ввода 4:
#  яблоко
#   груша
#   апельсин
#   лимон

# Пример вывода 4:
#    яблоко, груша, апельсин и лимон