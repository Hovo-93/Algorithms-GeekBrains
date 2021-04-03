"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile
import sys


@profile
def special(func):
    def countEvenDigits(num, an_even_numb=0, odd=0):
        func(num, an_even_numb=0, odd=0)
        if num == 0:
            return an_even_numb, odd
        else:
            lastDigit = num % 10
            firstDigit = num // 10
            if lastDigit % 2 == 0:
                an_even_numb += 1
            else:
                odd += 1
            return countEvenDigits(firstDigit, an_even_numb, odd)


profile(special(112243))


# Да есть подводные камни получаем много таблиц сколько вызовов функции столько и таблиц

#

def countEvenDigits(num, an_even_numb=0, odd=0):
    if num == 0:
        return an_even_numb, odd
    else:
        lastDigit = num % 10
        firstDigit = num // 10
        if lastDigit % 2 == 0:
            an_even_numb += 1
        else:
            odd += 1
        return countEvenDigits(firstDigit, an_even_numb, odd)


print(sys.getsizeof(countEvenDigits(112243)), 'байт')
