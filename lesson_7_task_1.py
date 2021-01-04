#-*-coding: utf-8-*-
'''
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
'''
import random
def bubble_sort(date: list):
    n = 1
    while n < len(date):
        for i in range(len(date) - 1):
            if date[i] > date[i + 1]:
                date[i], date[i + 1] = date[i + 1], date[i]
        n += 1
    return date

def bubble_sort2(date: list):
    for i in range(len(date)-1): # кажется for должен быть быстрее
        for j in range(i, len(date)-1):
            if date[j] > date[j + 1]:
                date[j], date[j + 1] = date[j + 1], date[j]
    return date

MAX = 100
MIN = -100
LENGTH_ARR = 20

arr = [random.randrange(MIN, MAX) for i in range(LENGTH_ARR)]

print(arr)
print(bubble_sort(arr))
print(bubble_sort2(arr))
