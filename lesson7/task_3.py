"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
Задачу можно решить без сортировки исходного
массива.
Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
[5, 3, 4, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 4, 5]
my_lst
new_lts
arr[m]
from statistics import median
[3, 4, 3, 3, 5, 3, 3]
left.clear()
right.clear()
m = 3
len = 7
i
left = []
right = []
left == right and
for i in
    for
    left == right
    left.clear()
    right.clear()
"""
import random

m = random.randint(1, 8)
org = [random.randint(1, 15) for _ in range(2 * m + 1)]
print(org)


def gnomeSort(arr):
    index = 0
    middle_el = len(arr) // 2

    while index < len(arr):
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1

    return arr[middle_el]


print(gnomeSort(org))
