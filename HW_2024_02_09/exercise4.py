# Задание 4.

chess_square1 = input('Введите название первой клетки шахматной доски: ') # вводим координаты в переменные первой и второй клетки
chess_square2 = input('Введите название второй клетки шахматной доски: ')

# Вычисления. Значения клеток перевожу в десятичную систему исчисления. Для этого использую функцию ord для буквы, и int - для перевода цифры из строки в целое число. Все вместе объединяем и проверяем на остаток от двух - так как на шахматной доске клетки либо черные либо белые.

a = (ord(chess_square1[0]) + int(chess_square1[1])) % 2

b = (ord(chess_square2[0]) + int(chess_square2[1])) % 2

# Задаю условие: значения совпадают - консоль отображает 'да'. И наоборот: значения разные - отображает 'нет'.

if a == b:
    print('Да')
else:
    print('Нет')

# Проверка
# Введите название первой клетки шахматной доски: a6
# Введите название второй клетки шахматной доски: b7
# Да

# Введите название первой клетки шахматной доски: e1
# Введите название второй клетки шахматной доски: h7
# Нет
    
#####
# Комментарий преподавателя:
# Хорошее решение. =)