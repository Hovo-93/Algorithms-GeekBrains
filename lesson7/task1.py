"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в
виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
import timeit
import random

orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)


# orig_list = [9,8,7,5,4,3,2,1]

def buuble(orig_list):
    last_item = len(orig_list) - 1
    for z in range(0, last_item):  # Для работы цикла z раз
        for i in range(0, (last_item - z)):  # Меньше циклов пробегов
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]

    return orig_list


print(buuble(orig_list))
orig_list = [random.randint(-100, 100) for _ in range(10)]

print(
    timeit.timeit(
        "buuble(orig_list[:])",
        globals=globals(),
        number=1000), 'По убыванию')


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000), 'По возрастанию')
# Первая функция Buuble() быстрее чем buuble_sort(),в buuble() искоючили лишние цикли пробеги
# Дороботка помогла нам в скорости
