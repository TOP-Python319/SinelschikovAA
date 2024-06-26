# Задание  3.

list1 = list(input())
list2 = list(input())
del list1[1::2]
del list2[1::2]
x = 'да'
y = 'нет'

for i in range(len(list1) - len(list2) + 1):
       if list2[i] in list1[i]:
              print(x)
              break
       else:
              print(y)
              break

print(list1)
print(list2)

# Пример ввода 2:
# 1 2 3 4
#    2 4

# Пример вывода 2:
# нет

# Комментарий преподавателя:

# list(input()) формирует список символов, а не целых чисел.
# Для создания списка целых чисел нужно использовать
# list(map(int, input().split())).

# del list1[1::2] и del list2[1::2] удаляют элементы с нечетными индексами,
# что не соответствует условиям задачи.
# Программа должна проверять, можно ли получить
# второй список из первого без изменения порядка элементов и без удаления.

# Цикл for сразу выводит "да" или "нет" на первой итерации из-за использования break.
# Это не даст правильного результата для всех возможных случаев.

# Последние две строки print(list1) и print(list2) не имеют смысла в контексте
# данной задачи и могут быть удалены.