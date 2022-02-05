i = 0
s = 0
ch = 0
nch = 0
maxValue = 0
minValue = 0
while True:
    q = int(input("Введите целое число: "))
    if q == 0:
        break
    if q % 2 == 0:
        ch += 1
    else:
        nch += 1
    if q > maxValue or maxValue == 0:
        maxValue = q
    elif q < minValue or minValue == 0:
        minValue = q
    i += 1
    s += q
print("Ввод закончен")
print("Количество введенных чисел: ", i)
print("Сумма чисел: ", s)
print("Cреднее арифметическое всех введённых чисел:", s / i)
print('Количество чётных чисел: ', ch)
print('Количество не чётных чисел: ', nch)
print("Min: ", minValue)
print("Max: ", maxValue)