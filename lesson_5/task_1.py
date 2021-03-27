"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import deque

companies = {}
profitable_companies = deque()
unprofitable_companies = deque()

n = int(input("Введите количество предприятий "))
for i in range(1, n + 1):
    name_companies = input(f"Введите наименование {i}-го предприятия ")
    profit = 0
    quarterly_profit = input('Ввдите прибиль за каждый квартал через пробел ').split()
    if len(quarterly_profit) > 4:
        print('Всего 4 квартала--Error')
        exit()
    for j in range(len(quarterly_profit)):
        profit += int(quarterly_profit[j])
        companies[name_companies] = profit
company_profit = 0
for key, value in companies.items():
    company_profit += value
average_profit = round(company_profit / n, 2)

for key, value in companies.items():
    if value > average_profit:
        profitable_companies.append(value)
    else:
        unprofitable_companies.append(value)
print(f"Средняя прибыль за год для всех предприятий: {average_profit}")
print(f"Компании с прибылью выше среднего: {profitable_companies}")
print(f"Компании с прибылью ниже среднего: {unprofitable_companies}")
