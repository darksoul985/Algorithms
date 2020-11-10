# -*- coding: utf-8 -*-
'''
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
максимальным элементами. Сами минимальный и максимальный элементы в сумму
не включать.
'''

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

arr_copy = []

for i in arr: # Создаем список уникальных значений
    if i not in arr_copy:
        arr_copy.append(i)

max_el = MIN_ITEM
min_el = MAX_ITEM
sum_el = 0

for i in arr_copy: # Находим минимальный и максимальный значения
    if i > max_el:
        max_el = i
    if i < min_el:
        min_el = i

for i in arr: # Суммируем
    if i != min_el and i != max_el:
        sum_el += i

print(f'Сумма элементов за исключением минимального {min_el} и максимального {max_el} составляет {sum_el}')