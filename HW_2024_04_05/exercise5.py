# Задание 5.

with open("input.txt", "r", encoding='utf-8') as text: #сначала открываем имеющийся файл input
    content = text.readlines() 

with open("output.txt", "w", encoding='utf-8') as text: # затем изменяем и записываем из input в созданный нами оutput
    for index, line in enumerate(content, start=1): # отделяем индекс и строку енумерейтом начиная (задать вопрос насчет индекса)
        text.write(f'{index}) {line}')

# 1) abcd
# 2) xcnvmnvkje
# 3) 32432423
# 4) sdflsdjkn34r43
# 5) 345349854395#$%$#
# 6) jksdfkjsdfkjsd
# 7) lwerjlwerlkwe
# 8) jwfhjkwehkjwefkjwebfjkwe
# 9) djdddddddddddddddddddddddddddddddd
# 10) 3249835438594390583490583490853490582349058340
# 11) sdfsjkldflksdjaflkjsdflkjsdlfkjsdlfjsldfsldkfjlsdkfjls