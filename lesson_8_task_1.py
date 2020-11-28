# -*-coding: utf-8 -*-
'''
1) Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
'''
import hashlib

def count_sub(s):
    subs_set = set()
    len_str = len(s)
    if len_str == 0:
        return f'Введена пустая строка'
    for i in range(len_str):
        for j in range(len_str-1 if i == 0 else len_str, i, -1):
            subs_set.add(hash(s[i:j]))

    return len(subs_set)

print(count_sub('papa'))
print(count_sub('sova'))
print(count_sub(''))
