"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять задачи с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import random

from memory_profiler import profile


########## Поиск четного числа ############
# func1 23.9219 MiB
@profile(precision=4)
def func1():
    x = list(range(100000))
    res = []
    for i in x:
        if i % 2 == 0:
            res.append(i)
    return res


# func2 20.3555 MiB
@profile(precision=4)
def func2():
    res = [x for x in range(100000) if not x % 2]
    return res


if __name__ == '__main__':
    func1()
    func2()


# По циклу 23.9219 MiB , list comprehension  20.3555 MiB

########### Заполнение списка и словаря программно ##########
# 20.6523 MiB
@profile(precision=4)
def app():
    n = range(100000)
    d = {}
    for i in n:
        key = range(random.randint(0, 10000))
        d[key] = str(i)
    return d


# 23.7070 MiB
@profile(precision=4)
def add():
    n = list(range(100000))
    m = []
    for i in n:
        m.append(i)
    return m


if __name__ == '__main__':
    app()
    add()
# Заполнение словаря  20.6523 MiB список 23.7070 MiB

##############Сортировка################
# 23.7656 MiB
count = 1000


@profile(precision=4)
def bubble_sort():
    mas = list(range(count))
    n = len(mas) - 1
    for z in range(0, n):
        for i in range(n):
            if mas[i] > mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
    return mas


def search_min(array):
    min_index = 0
    for i in range(len(array)):
        if array[i] < array[min_index]:
            min_index = i

    return min_index


# 27.7852 MiB
@profile(precision=4)
def my_worst_sort():
    mas = list(range(count))
    sorted_mas = []
    steps = [mas]  # Шаги для использования лишней памяти
    while len(steps[len(steps) - 1]) > 0:
        current = steps[len(steps) - 1]
        i = search_min(current)
        sorted_mas.append(current[i])

        new_mas = current.copy()
        new_mas.pop(i)
        steps.append(new_mas)

    return sorted_mas


if __name__ == '__main__':
    bubble_sort()
    my_worst_sort()
# bubble_sort() использует 23.7656 MiB памяти, my_worst_sort() 27.7852 MiB
