import random

rangeStart = int(input("Введите начало диапазона: "))
rangeEnd = int(input("Введите конец диапазона: "))
if rangeStart >= rangeEnd:
    print("Некорректное значение начала/конца.")
    exit()

size = int(input("Введите размер диапазона: "))
if size < 1:
    print("Некорректный размер.")
    exit()

a = random.sample(range(rangeStart, rangeEnd), size)
print("Ваша строка: ", a)

k = int(input("Введите индекс числа: "))

for i in range(k, len(a)-1):
    a[i], a[i+1] = a[i+1], a[i]
print("Сместили число с заданным индексом в конец: ", a)
a.pop()
print("Удалили число с заданным индексом в конеце: ", a)