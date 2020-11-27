#-*-coding: utf-8-*-
'''
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''
import random
def merge(left, rigth):
    sort_list = []
    left_idx = rigth_idx = 0

    left_len, rigth_len = len(left), len(rigth)
    for _ in range(left_len + rigth_len):
        if left_idx < left_len and rigth_idx < rigth_len:
            if left[left_idx] <= rigth[rigth_idx]:
                sort_list.append(left[left_idx])
                left_idx +=1
            else:
                sort_list.append(rigth[rigth_idx])
                rigth_idx += 1
        elif left_idx == left_len:
            sort_list.append(rigth[rigth_idx])
            rigth_idx +=1
        elif rigth_idx == rigth_len:
            sort_list.append(left[left_idx])
            left_idx += 1
    return sort_list

def merge_sort(date: list): # делим список пополам до длины 1 элемента
    if len(date) <= 1:
        return date
    elif len(date) == 2:
        if date[0] > date[1]:
            date[0], date[1] = date[1], date[0]
        return date
    mid = len(date) // 2
    left = merge_sort(date[:mid])
    right = merge_sort(date[mid:])

    return merge(left, right)

MAX = 50
MIN = 0
LENGTH_ARR = 20

arr = [random.uniform(MIN, MAX) for i in range(LENGTH_ARR)]
print(merge_sort(arr))