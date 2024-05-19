# Задание  4.

dict = {}
while True:
    user_input = input("введите команду ")
    if not user_input :
        break
    else :
        key, value = user_input.split()
        dict[key] = value

error_descr = input('Enter a description of the error: ')

try :
    key = next(key for key, value in dict.items() if value == error_descr)

except StopIteration :
    key = '! value error !'
print(key)

# введите команду 1004 ER_CANT_CREATE_FILE
# введите команду 1005 ER_CANT_CREATE_TABLE
# введите команду 1006 ER_CANT_CREATE_DB
# введите команду 
# Enter a description of the error: ER_CANT_CREATE_FILE
# 1004

# Комментарий преподавателя:
# Имя переменной dict может создать путаницу, так как dict является 
# встроенным типом данных в Python.
# Лучше использовать другое имя, например, my_dict.