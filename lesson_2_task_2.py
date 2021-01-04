# -*- coding:utf-8 -*-

'''
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено
число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

def counter (num, even=0, odd=0)-> str:
    if num == 0:
        return f'В числе {number}\nЧетных цифр: {even}\nНечетных цифр: {odd}'
    elif (num % 10 % 2) == 0:
        even += 1
    else:
        odd += 1
    return counter(num // 10, even, odd)

number = int(input('Введите целое число:\n'))
print(counter(number))