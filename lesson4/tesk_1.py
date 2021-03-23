"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


s = """
def func_1(nums):
        new_arr = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                new_arr.append(i)
        return new_arr
"""
result1 = (timeit.timeit(s, number=10000, globals=globals()))

print(timeit.timeit(s, number=10000, globals=globals()))


def func_2(nums):
    new_arr = []
    for i, j in enumerate(nums):
        if j % 2 == 0:
            new_arr.append(i)
    return new_arr


s1 = """
def func_2(nums):
    new_arr = []
    for i,j in enumerate(nums):
        if j % 2 == 0:
            new_arr.append(i)
    return new_arr
"""
result2 = (timeit.timeit(s1, number=10000, globals=globals()))

print(timeit.timeit(s1, number=10000, globals=globals()))
if result1 > result2:
    print('Func_2 быстрее чем Func_1')
else:
    print('Func_1 быстрее чем Func_2')

# """ В 'func(2)' данном случае на каждой итерации цикла из объекта enumerate извлекается очередной--> 'кортеж',
#  состоящий из индекса очередного элемента списка и значения этого элемента .По этому быстрее
#  И так как enumerate() функция  в Python Встроенная она будет работать самым быстрим алгоритмом
# """
