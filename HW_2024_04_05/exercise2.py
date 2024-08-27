with open("data.txt", "r", encoding='utf-8') as text:
    files = text.readlines()
    for line in reversed(files): # используем reverse
        print(line, end="")

# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.