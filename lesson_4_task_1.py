#-*-coding: utf-8-*-
'''
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
'''
# 4. Определить, какое число в массиве встречается чаще всего.

import random
import timeit as tit

def arr(size):
    MIN_ITEM = 0
    MAX_ITEM = 10000
    arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    return arr


print('******первый алгоритм******')
ones = '''
n = [0]
frequency = 1
for i in range(len(array)):
    spam = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            spam += 1
    if spam > frequency:
        frequency = spam
        n = array[i]
'''

array = arr(10)
print(tit.timeit(ones, number=1000, globals=globals())) # 0.013734614999975747 N = 10
array = arr(100)
print(tit.timeit(ones, number=1000, globals=globals()))  # 0.6031229830000484 N = 100
array = arr(1000)
print(tit.timeit(ones, number=1000, globals=globals()))  # 54.34004129300001 N = 1000

print('****второй алгоритм****')

two = '''
m = set(array) # оставляем только уникальные значения

max = 0
val = 0
if len(m) == len(array): # если длина списков равна, все элементы уникальны
    max = 1
else:
    for i in m:
        if array.count(i) > max:
            max = array.count(i)
            val = i
'''

array = arr(10)
print(tit.timeit(two, number=1000, globals=globals())) # 0.0004248850000294624 N = 10
array = arr(100)
print(tit.timeit(two, number=1000, globals=globals())) # 0.0028529969999908644 N = 100
array = arr(1000)
print(tit.timeit(two, number=1000, globals=globals())) # 14.535517098000128 N = 1000

print('****третий алгоритм****')
three = '''
count_1 = {} # Используем список
freak = 1
num = None
for i in array:
    if i in count_1:
        count_1[i] += 1
    else:
        count_1[i] = 1

    if count_1[i] > freak:
        freak = count_1[i]
        num = i
'''
array = arr(10)
print(tit.timeit(two, number=1000, globals=globals())) # 0.0006145690003904747 N = 10
array = arr(100)
print(tit.timeit(two, number=1000, globals=globals())) # 0.002782613999897876 N = 100
array = arr(1000)
print(tit.timeit(two, number=1000, globals=globals())) # 14.493449969999801 N = 1000

'''
Вывод: лучший алгоритм №3, поскольку у него линейное время выполенения O(n)
алгоритм №2 хуже, поскольку в любом случае проходит массив дважды, однако за счет
создания списка уникальных значений делает это быстрее первого, кроме того
метод count написанный на C обходит массив значительн быстее O(n) 
и по времени лишь немного уступает алгоритаму 3
Худший алгоритм №1.
'''