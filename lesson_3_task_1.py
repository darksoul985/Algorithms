# -*- coding: utf-8 -*-
'''
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
каждому из чисел в диапазоне от 2 до 9.
'''

start_range = 2
end_range = 100

multiples_min = 2
multiples_max = 9 + 1

for i in range(multiples_min, multiples_max):
    count = 0
    for itm in range(start_range, end_range):
        if (itm % i) == 0:
            count += 1
    print(f'Числу {i} в диапазоне от {start_range} до {end_range-1} кратны {count} чисел')