"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым
"""
from itertools import groupby
from operator import itemgetter
from timeit import timeit

from win32com.test.testCollections import L

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(timeit("func_1()", globals=globals()))


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(timeit("func_2()", globals=globals()))


def max_occurrences_3b(seq=L):
    "sort groupby list comprehension"
    return max([(k, sum(1 for i in g)) for k, g in groupby(sorted(seq))], key=itemgetter(1))


print(timeit("max_occurrences_3b", globals=globals()))

print(func_1())
print(func_2())
print(max_occurrences_3b(array))
"""
С помощью функции 'max_occurrences_3b' удалось ускорить . Импортировал groupby--> Функция выдаёт кортежи 
из двух элементов.
Первый элемент: значение, возвращённое функцией key.
Второй элемент: итератор по объектам, попавшим в группу.
"""