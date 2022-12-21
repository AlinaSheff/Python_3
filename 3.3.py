# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform
list = []
for i in range(5):
    list.append(uniform(1, 10))
print(list)

for i in range(len(list)):
    list[i] = round(list[i] - int(list[i]), 2)
print(list)
print(max(list) - min(list))   
