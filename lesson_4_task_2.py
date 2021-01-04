#-*-coding: utf-8-*-
'''
2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа
должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:
sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2
'''
import cProfile
import timeit as tit
# 1
def sieve(num):
    if num == 0:
        return 2
    else:
        counter = 2
        current_num = 3
        while counter < num:
            current_num += 1
            for i in range(2, current_num):
                if current_num % i == 0:
                    break
            else:
                counter += 1
    return current_num
# 2
def sieve_1(num):
    lst = [2]

    for i in range(3, num ** 2, 2):
        if len(lst) == num:
            break
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst[-1]

print(tit.timeit('sieve(50)', number=1000, globals=globals())) # 0.3474250340004801
print(tit.timeit('sieve(100)', number=1000, globals=globals())) # 1.3616845999995348
print(tit.timeit('sieve(200)', number=1000, globals=globals())) # 6.318587707000006
print('****')
print(tit.timeit('sieve_1(50)', number=1000, globals=globals())) # 0.06403868500001408
print(tit.timeit('sieve_1(100)', number=1000, globals=globals())) # 0.16733597799975541
print(tit.timeit('sieve_1(200)', number=1000, globals=globals())) # 0.42271230700043816

cProfile.run('sieve(10000)')

'''
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   31.215   31.215 <string>:1(<module>)
        1   31.215   31.215   31.215   31.215 lesson_4_task_2.py:24(sieve)
        1    0.000    0.000   31.215   31.215 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''

cProfile.run('sieve_1(10000)')

'''
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.165    0.165 <string>:1(<module>)
        1    0.157    0.157    0.165    0.165 lesson_4_task_2.py:39(sieve_1)
        1    0.000    0.000    0.165    0.165 {built-in method builtins.exec}
    52365    0.006    0.000    0.006    0.000 {built-in method builtins.len}
     9999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

'''
Извиняюсь, но 1 из алгоритмов взял Ваш, голову сломал на поиске n в ряде простых чисел
Еще не до конца разбираюсь в асимптотическом анализе, но по результатам алгоритм №2 несмотря на 
двойную вложенность циклов оказался лучше как с точки зрения времени выполнения так и 
скорости работы составных частей. Однозначно, цикл for работает быстрее while.
В первом алгоритме потери идут именно на проверке булевого значения в цикле while 
'''