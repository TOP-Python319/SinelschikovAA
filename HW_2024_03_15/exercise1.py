#  Задание  1.

mail = str(input()) # переменная строки почты

if '@' in mail and '.' in mail: # задаем условие - если в строке есть символ "собачки" и точки
    print('да') # программа отображает "да"
else:
    print('нет') # в противном случае - нет

# Проверка
# Пример ввода 1: sgd@ya.ru
# Пример вывода 1: да
    
# Пример ввода 2: abcde@fghij
# Пример вывода 2: нет

# Комментарий преподавателя:
# Проверка наличия '@' и '.' недостаточна, так как не гарантирует,
# что '.' идет после '@'.