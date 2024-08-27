# Задание 6.

def from_base(num_str, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    num_str = num_str.lower()

    num = 0
    for i in num_str:
        num = num * base + digits.index(i)
    return num

def to_base(num, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if num == 0:
        return '0'

    res = ''
    while num > 0:
        res = digits[num % base] + res
        num //= base
    return res

def int_base(num_str: str, base_source: int, base_target: int) -> str:
    if base_source < 2 or base_source > 36 or base_target < 2 or base_target > 36:
        return None

    try:
        num = from_base(num_str, base_source)
        new_num_str = to_base(num, base_target)
        return new_num_str
    except ValueError:
        return None
print(int_base('ff00', 16, 2))  
print(int_base('1101010', 2, 30))  

# 1111111100000000
# 3g