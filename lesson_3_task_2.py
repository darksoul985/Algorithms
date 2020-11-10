# -*- coding: utf-8 -*-

'''
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо
заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в
этих позициях первого массива стоят четные числа.
'''
from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

first_range = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
second_range = []

for idx, vol in enumerate(first_range):
    if vol % 2 == 0:
        second_range.append(idx)

print(f'В массиве {first_range} четные элементы под индексами {second_range}')