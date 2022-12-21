# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
list = []
for i in range(5):
    list.append(randint(1, 10))
print(list)

x = len(list)-1
for i in range(x):
    if i <= x:
        mult = 1
        mult *= (list[i] * list[x])
        x -= 1
        print(mult, end=" ")