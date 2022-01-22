year = int(input("Введите год: "))

if year % 400 == 0 and year % 4 == 0 and year % 4 == 0:
 print("Високосный")
else:
    print("Не високосный")