"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям
И добавить аналитику, так ли это или нет.!
"""

from collections import deque
import timeit

a = [1, 2, 3, 4, 5, 6]  # input('Введите число через пробел ').split()
b = deque('123456')  # deque(input('Введите число '))

s = """a.insert(0, 7)
"""
print(timeit.timeit(s, number=10000, globals=globals()), 'Встака по индексу')

s1 = """
b.appendleft(7)
"""
print(timeit.timeit(s1, number=10000, globals=globals()), 'Добавление элем. через appendleft')

# Добавления элементов по циклу в начало списка
s2 = """
musical_notes = ["C", "D", "E", "F", "G", "A"]
for i in musical_notes:
    a.insert(0,i)
"""
print(timeit.timeit(s2, number=100, globals=globals()), 'Добавление в начало по циклу')

# Добавление в начало дека
s3 = """
b.extendleft([8,9])
"""
print(timeit.timeit(s3, number=100, globals=globals()), 'Добавление через extendleft')
s4 = """
    a.pop(0)
"""
print(timeit.timeit(s3, number=100, globals=globals()), 'Удаление первого элем. в списке')
s5 = """
b.popleft()
"""
print(timeit.timeit(s3, number=100, globals=globals()), 'Удаление первого элем. в списке через popleft')

print(a[3])  # В списке константная  время
print(b[3])  # В деке это операция линейная O(n)

print(timeit.timeit('a.reverse()', number=100, globals=globals()), 'Reverse список')
# Здесь быстрее потому что знает где голова, где хвост
print(timeit.timeit('b.reverse()', number=100, globals=globals()), 'Revers дека')

"""В итоге, Деке extendleft,popleft ,appnedleft  быстрее чем та же операция в списке,но если в деке взять
 элемент по индексу то скорость получаетсья в разы медленне чем у списков
"""

print(timeit.timeit('a.reverse()', number=100, globals=globals()), 'Reverse список')
print(timeit.timeit('b.reverse()', number=100, globals=globals()), 'Revers дека')
