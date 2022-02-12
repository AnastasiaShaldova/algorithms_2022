"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для пятого скрипта
"""
from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


@memory
class ComplexNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сложение комплексных чисел')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Умножение комплексных чисел')
        return f'z = {self.a * other.a - self.b * other.b}*{self.b * other.a + self.a * other.b} * i'


@memory
class ComplexNumbersTwo:
    __slots__ = ('a', 'b')

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сложение комплексных чисел')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Умножение комплексных чисел')
        return f'z = {self.a * other.a - self.b * other.b}*{self.b * other.a + self.a * other.b} * i'


a = ComplexNumbers(1, -2)
b = ComplexNumbers(3, 4)
print(a + b)
print(a * b)


a = ComplexNumbersTwo(1, -2)
b = ComplexNumbersTwo(3, 4)
print(a + b)
print(a * b)

"""Использование слотов, существенно влияет на память. 
Потребление памяти заметно меньше."""