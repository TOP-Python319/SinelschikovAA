# Задание 3.

# Создаем функцию numbers_strip.

def numbers_strip(numbers_list: list[float], n: int=1, copy: bool=False):
    if copy:   # если параметр copy равен True    
        return numbers_list.copy() # копируем список со значениями
    else :
        for _ in range(n): # создаем цикл который будет повторяться n раз
            numbers_list.remove(min(numbers_list)) # удаляем минимальное значение в списке
            numbers_list.remove(max(numbers_list)) # удаляем минимальное значение в списке
        return numbers_list # возвращаем спиок

sample = [1, 2, 3, 4] # создаем список
sample_stripped = numbers_strip(sample) # вызываем функцию
print(sample_stripped) # выводим результат

#[2, 3]

sample = [10, 20, 30, 40, 50]
sample_stripped = numbers_strip(sample, 2, copy=True)
print(sample_stripped)

#[10, 20, 30, 40, 50]