"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ """


def division(arg1, arg2):
    try:

        result = arg1 / arg2
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return round(result)


def is_correct_operator(operator):
    return operator == '0' or operator == '+' or operator == '-' or operator == '*' or operator == '/'


def calcutation():
    a = int(input("Введите первое число "))
    b = int(input("Введите второе число "))
    op = input("Введите знак операции ")

    if op == '0':
        return "Программа завершена "

    if b == 0 and op == '/':
        return division(a, b)

    if not is_correct_operator(op):
        print('Wrong operator')
        return calcutation()

    elif op == '+':
        res = a + b
        print(f"Ваш результат: {res}")
        return calcutation()

    elif op == '-':
        res = a - b
        print(f"Ваш результат: {res}")
        return calcutation()
    elif op == '*':
        res = a * b
        print(f"Ваш результат: {res}")
        return calcutation()
    else:
        res = a / b
        print(f"Ваш результат: {res}")
        return calcutation()


print(calcutation())
