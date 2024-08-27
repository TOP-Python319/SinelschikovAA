# Задание 2.

# задаем функцию taxi_price - в ней будет два параметра: дистанция и время ожидания, все данные будет введены как строка. Начальное значение времени ожидания равно нулю.

def taxi_price(distance: int, waiting_time: int=0):
    if distance < 0 or waiting_time < 0: # если оба показателя меньше нуля - возвращаем None
        return None
    
# Проводим расчет стоимости.

    taxi_cost = 80 # цена базовой стоимости
    distance_cost = (distance / 150) * 6 # добавляем 6 рублей за каждые 150 метров проезда - и добавляем к стоимости
    waiting_time_cost = waiting_time * 3 # каждая минута ожидания такси добавляет 3 рубля к стоимости
    result = taxi_cost + distance_cost + waiting_time_cost # итоговая сумма - которую округляем до целого числа.

    if distance == 0: # если дистанция равна нулю - мы возвращаем средства.
        return taxi_cost + 80 + waiting_time_cost

    return round(result)

print(taxi_price(1500))
# 140
print(taxi_price(2560))
# 182
print(taxi_price(0, 5))
# 175
print(taxi_price(42130, 8))
# 1789
print(taxi_price(-300))
# None