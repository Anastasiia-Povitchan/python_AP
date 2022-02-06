import random

rangeStart = int(input("Введите начало диапазона: "))
rangeEnd = int(input("Введите конец диапазона: "))
if rangeStart >= rangeEnd:
    print("Некорректное значение начала/конца диапазона")
    exit()

size = int(input("Введите размер диапазона: "))
if size < 1:
    print("Некорректный размер.")
    exit()

a = random.sample(range(rangeStart, rangeEnd), size)
print("Заданные значениея: ", a)
s = 0
for i in range(1, len(a)-1):
    if a[i-1] < a[i] > a[i+1]:
        s += 1
print("Количество элементов которые больше своих 2х соседей: ", s)
