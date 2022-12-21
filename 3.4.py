# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input("Введите число: "))
x = ""
while num > 0:
    x = str(num % 2) + x
    num //=2
print(f'В двоичной системе исчисления: {x}')