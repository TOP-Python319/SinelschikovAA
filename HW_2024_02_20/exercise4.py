# Задание  4.

x = int(input('n = ')) # количество разрядов для числа
end_x = int('1' + '0' * x) # последнее число в диапазоне заданного разряда
start_x = end_x // 10 # начальное число в диапазоне заданного разряда

count = 0 # переменная счетчика

for i in range(start_x, end_x):
    for j in range(2, i):
        if i % j == 0:
            break
        if i % j != 0 and j == i - 1:
            count += 1

print(f'{count}')

# n = 3
# 143


# комментарий преподавателя:
# всё верно!