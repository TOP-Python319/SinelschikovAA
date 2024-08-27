# Задание 3.

import re

with open("nums.txt", "r", encoding='utf-8') as text:
    files = text.read()
    number = re.findall(r'\d+', files) # создаем число которое будет сохранять поиск всех цифр в строках
    total = 0
    for num in number:
        total += int(num) # суммируем в тотал каждое найденное число 

    print(total)


    # 124410