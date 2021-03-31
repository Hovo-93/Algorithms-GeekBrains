"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
import timeit
from decimal import Decimal

origin_list = [random.uniform(0, 50) for _ in range(5)]
print(*origin_list, 'Не отсортированном виде')


def merge_two_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(s):
    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left, right)


print(*merge_sort(origin_list), 'В отсортированном виде')

# Длина 10
origin_list = [random.uniform(0, 50) for _ in range(10)]
print(
    timeit.timeit(
        "merge_sort(origin_list[:])",
        globals=globals(),
        number=1000))
# Длина 100
origin_list = [random.uniform(0, 50) for _ in range(100)]
print(
    timeit.timeit(
        "merge_sort(origin_list[:])",
        globals=globals(),
        number=1000))
# Длина 1000
origin_list = [random.uniform(0, 50) for _ in range(1000)]

print(
    timeit.timeit(
        "merge_sort(origin_list[:])",
        globals=globals(),
        number=1000))
