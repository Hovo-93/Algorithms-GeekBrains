"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
import timeit

NEW_DICT = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)

NEW_DICT = {'a': 1, 'b': 2, 'c': 3}  # -> с версии 3.6 порядок сохранится
print(NEW_DICT)

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
new_orderidict = """collections.OrderedDict(sorted(d.items(), key=lambda t: t[0]))"""

print(timeit.timeit(new_orderidict, number=100, globals=globals()), 'Скорость работы OrderDict')
# Обычный Словарь
original_dict = """d = {'a': 10, 'b': 15, 'c': 4}
list_keys = list(d.keys())
list_keys.sort()
"""
print(timeit.timeit(original_dict, number=100, globals=globals()), 'Скорость работы обычного словарья')

c = collections.OrderedDict.fromkeys('abcde')
c.move_to_end('b')
print(''.join(c.keys()))

c.move_to_end('b', last=False)
print(''.join(c.keys()))

t1 = """original =  {'a': 10, 'b': 15, 'c': 4}
original.update({'item3': 3})
print(original)
"""
print(timeit.timeit(original_dict, number=100, globals=globals()), 'Скорость добавления элемента ')

t2 = """order_dict = collections.OrderedDict({'a': 10, 'b': 15, 'c': 4})
order_dict.update({'item2':1})
print(order_dict)
"""
print(timeit.timeit(original_dict, number=100, globals=globals()), 'Скорость добавления элемента с Orderdict')

# Обычный словарь  быстрее работает чем Orderdict
# Есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях -мой ответ нету смысла
