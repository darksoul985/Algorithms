# -*- coding: utf-8 -*-
'''
3. В массиве случайных целых чисел поменять местами минимальный
и максимальный элементы.
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

for i in arr_copy: # Находим минимальный и максимальный значения
    if i > max_el:
        max_el = i
    if i < min_el:
        min_el = i

print(f'Первоначальный список {arr}')

for idx, val in enumerate(arr): # Заменяем
    if val == min_el:
        arr[idx] = max_el
    elif val == max_el:
        arr[idx] = min_el

print(f'Список с замененными элементами {arr}')