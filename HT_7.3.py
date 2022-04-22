# var_1

from random import randint
import random

spisok = []
for i in range(5):
    spisok.append(random.randint(0,2))

spisok1 = list(set(spisok))
spisok2 = dict.fromkeys(list(set(spisok)))

for i in spisok1:
    spisok2[i] = spisok.count(i)

print(spisok)
print(spisok2)


# var_2
list = [9, 13, 1, 3, 7, 3, 1, 1, 7, 1, 7, 9]
dict = {}

for el in list:
    if dict.get(el, None):
        dict[el] += 1
    else:
        dict[el] = 1
print(dict)
