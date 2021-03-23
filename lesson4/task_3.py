"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Сделайте вывод, какая из трех реализаций эффективнее и почему!!!
И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
from cProfile import run
from timeit import timeit


# Рекурсия
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


n1 = 12345
print(timeit("revers_1(n1)", globals=globals()), 'Рекурсия')
run("revers_1(n1)")


# Цикл
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


n2 = 12345
print(timeit("revers_2(n2)", globals=globals()), 'Цикл')
run("revers_2(n2)")


# 'Slicing'
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]  # O(n)
    return revers_num  # O(1)


n3 = 12345
print(timeit("revers_3(n3)", globals=globals()), 'Slicing')
run("revers_3(n3)")


# Линейная сложность
def revers_4(enter_num):
    enter_num = str(enter_num)  # O(1)
    revers_num = []
    for o in reversed(enter_num):  # O(n)
        revers_num.append(o)  # O(1)
    return revers_num  # O(1)


n4 = 12345
print(timeit("revers_4(n4)", globals=globals()), 'Цикл for')
run("revers_4(n4)")

#  Из четырех реализаций эффективнее  revers_3()  0.6248117999999998,реализованно с помощью 'Slicing',
#  взяв элемент по индексу или срезом (slice) мы не как не меняем исходную коллекцию,
#  мы просто скопировали ее часть для дальнейшего использования .
