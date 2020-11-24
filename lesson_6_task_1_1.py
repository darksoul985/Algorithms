import sys
import collections

# Операционная система: Windows 10
# Разрядность ОС: 64
# Разрядность интерпретатора: win32

def get_book_var(modul_name): # получаю все переменные модуля
    module = globals().get(modul_name, None)
    book = {}
    if module:
        book = {key: value for key, value in module.__dict__.items() if not (
        key.startswith('__') or key.startswith('_') or hasattr(value, '__loader__')
        or hasattr(value, '__coll__')
        )}

    return book

def deep_getsuzeof(o, ids): # тут я, конечно, воспользовался помощью коллег))
    d = deep_getsuzeof
    if id(o) in ids:
        return 0

    r = sys.getsizeof(o)
    ids.add(id(o))

    if isinstance(o, str):
        return r

    if isinstance(o, collections.abc.Mapping):
        return r + sum(d(k, ids) + d(v, ids) for k, v in o.iteritems())

    if isinstance(o, collections.abc.Container):
        return r + sum(d(x, ids) for x in 0)

    return r

import lesson_6_task_1

book = get_book_var('lesson_6_task_1')

summ = 0

for key, value in book.items():
    summ += deep_getsuzeof(key, set())
    print(f'{type(value)=}, {sys.getsizeof(value)}, {key}')

print(f'Всего занимает: {summ}')
# Мои результаты
'''
type(value)=<class 'method'>, 64, randint
Константы:
type(value)=<class 'int'>, 28, SIZE
type(value)=<class 'int'>, 24, MIN_ITEM
type(value)=<class 'int'>, 28, MAX_ITEM
Созданный массив:
type(value)=<class 'list'>, 312, arr
Первый вариант:
type(value)=<class 'list'>, 248, n
type(value)=<class 'int'>, 28, i
type(value)=<class 'int'>, 28, max
type(value)=<class 'int'>, 28, val
Второй вариант:
type(value)=<class 'collections.Counter'>, 1192, cnt
type(value)=<class 'int'>, 28, key
type(value)=<class 'int'>, 28, value
type(value)=<class 'int'>, 28, max_1
type(value)=<class 'int'>, 28, val_1
Третий вариант:
type(value)=<class 'int'>, 28, val_2
type(value)=<class 'int'>, 28, max_2
type(value)=<class 'int'>, 28, spam
type(value)=<class 'int'>, 28, j
Всего занимает: 956

Вывод:
Третий вариант, пожалуй, самый экономный по памяти, так как хранит только список
со значением и количество повторений в виде числа (итого 28 * 4).
Первый вариант затарчивает больше памяти, ввиду хранения уникальных значений
в списке n, на что собственно и затрачиватеся память (итого 248 + 28 *3).
Второй вариант самый короткий по коду, но хранение коллекции Counter это капец
как затратно по памяти.

И я пока не понял, но общая сумма, почему то получилась меньше чем значение коллекции
На этом я застрял
'''