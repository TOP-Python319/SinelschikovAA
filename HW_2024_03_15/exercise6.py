# Задание 6.

binary = {"0", "1"}

string = input()

if string.startswith('0b'):
    string = string[2:]

if string.startswith('b'):
    string = string[1:]

if set(string) <= binary:
    print("да")
else:
    print("нет")

# Комментарий преподавателя:

# Можно отметить, что после удаления '0b' префикса не может быть префикса 'b',
# поэтому использование конструкции if-elif вместо двух отдельных if
# будет более логичным.
