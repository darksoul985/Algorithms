# -*- coding:utf-8 -*-

'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и
вывести на экран. Например, если введено число 3486, надо вывести 6843.
'''

num = int(input('Введите целое число:\n'))
result = 0

for i in str(num):
    result = result * 10 + num % 10
    num //= 10

print(f'Введенное число в обратном порядке {result}')