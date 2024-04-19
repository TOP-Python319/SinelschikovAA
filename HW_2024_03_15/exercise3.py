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