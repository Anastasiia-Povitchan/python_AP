a = int(input("Введите ЦЕЛОЕ, ПОЛОЖИТЕЛЬНОЕ, ТРЁХЗНАЧНОЕ число: "))

if a < 100 or a > 999:  # Проверка на внимательность :)
    print("Прочитай условие!")
else:
    q = a % 10
    w = a % 100 // 10
    e = a % 1000 // 100
    print("Перевернули: ", q * 100 + w * 10 + e)