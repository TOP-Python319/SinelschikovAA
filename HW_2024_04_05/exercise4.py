# Задание 4.

import random
with open("random.txt", "w", encoding='utf-8') as text:
    for r in range(25):
        random_num = random.randint(111, 777)
        text.write(str(random_num) + "\n")

# 742
# 582
# 502
# 736
# 147
# 390
# 500
# 666
# 290
# 616
# 416
# 325
# 749
# 749
# 420
# 245
# 495
# 567
# 723
# 637
# 612
# 555
# 770
# 582
# 544