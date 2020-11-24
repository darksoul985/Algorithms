#-*-coding: utf-8-*-

'''
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трех уроков. Проанализировать результат и определить
программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
● написать 3 варианта кода (один у вас уже есть);
● проанализировать 3 варианта и выбрать оптимальный;
● результаты анализа (количество занятой памяти в вашей среде разработки)
вставить в виде комментариев в файл с кодом. Не забудьте указать версию и
разрядность вашей ОС и интерпретатора Python;
● написать общий вывод: какой из трёх вариантов лучше и почему.
'''

'''
4. Определить, какое число в массиве встречается чаще всего.
'''
import sys
from random import randint
import collections


SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 100

arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# first option

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


# second option

cnt = collections.Counter()
for i in arr:
    cnt[i] += 1

for key, value in cnt.most_common(1):
    max_1 = key
    val_1 = value

# third option

val_2 = arr[0]
max_2 = 1
for i in range(len(arr)):
    spam = 1
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            spam += 1
    if spam > max_2:
        max_2 = spam
        val_2 = arr[i]
