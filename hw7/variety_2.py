from random import randint

a = [randint(0, 20) for i in range (5)]
b = [randint(0, 20) for i in range (5)]

print("Первый список:", a, '\n'"Второй список:", b)

print("Уникальные значение из 2х списков: ", set(a) ^ set(b))