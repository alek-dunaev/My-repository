"""Пример использования функции рандом"""


import random
randomlist = []
for i in range(5):
    m = random.randint(0,5)
    randomlist.append(m)

print(randomlist)

nmax = 0;
for i in randomlist:
        if i > nmax:
            nmax = i
print(randomlist)
print(nmax)
