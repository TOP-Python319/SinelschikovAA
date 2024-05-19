# Задание 5.

scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
} # список очков и слов

def callculation_score(word): # 
    score = 0 # создаем счетчик
    for letter in word.upper(): # перебираем буквы в инпуте
        for key, value in scores_letters.items(): # для ключа и значения в нашем списке scores_letters - 
            if letter in value: # если буквы из инпута в значениях (scores_letters.values) в списке то
                score += key # прибавляем счет
    return score


word = input().replace('Ё', 'Е')
print(callculation_score(word))

# Комментарий преподавателя:
# Для более компактного и читаемого кода можно использовать генераторные выражения
# для создания словаря scores_letters и для подсчета очков за слово.
# score = sum(key for letter in word for key, value in scores_letters.items() if letter in value)