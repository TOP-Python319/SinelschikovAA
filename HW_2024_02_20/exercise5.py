# Задание 5.

telegram = input('Введите текст телеграммы: ') # переменная для ввода текста телеграммы

price = (len(telegram) - telegram.count(' ')) * 30 # переменная стоимости телеграммы: из длины телеграммы вычитаем кол-во "совпадений" значений в строках. Умножаем все это на 30.

print(f'Цена телеграммы: {price // 100} руб. {price % 100} коп.')

# Введите текст телеграммы: грузите апельсины бочках братья карамазовы
# Цена телеграммы: 11 руб. 40 коп.

# Введите текст телеграммы: привет шлю телеграмму я учу python тчк
# Цена телеграммы: 9 руб. 60 коп.