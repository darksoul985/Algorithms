# -*- coding: utf-8 -*-
'''
4. Определить, какое число в массиве встречается чаще всего.
'''

from random import randint

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 100

arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

n = []

for i in arr:
    if i not in n:
        n.append(i)

max = 0
val = 0

for i in n:
    if arr.count(i) > max:
        max = arr.count(i)
        val = i

print(f'Чаще всего в массиве встречается число {val} в количестве {max}')