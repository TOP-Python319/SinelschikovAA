# Задание 1.

def strong_password(password: str):
    if len(password) < 8: # задаем условие - если длина пароля меньше восьми символов
        return False # возвращаем ошибку
    elif password.isupper() or password.islower(): # если символы только в верхнем или только в нижнем регистрах
        return False # возвращаем ошибку
    elif len(set(password) and set("'><:][@$%^&*)(#^:;?'=+-'_")) < 1: # проверяем наличие спецсимволов
        return False
    elif len(set(password) and set("1234567890")) < 2: # проверяем наличие минимум двух цифр в пароле
        return False
    else: # если все сходится - возвращаем значение True
        return True

print(strong_password('aP1:kD_l0')) # вызываем функции - с правильным и неправильным паролями
print(strong_password('password'))

# True
# False