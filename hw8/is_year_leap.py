def if_year_leap(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

_year = int(input("Введите год: "))

if if_year_leap(_year):
    print("Високосный")
else:
    print("Не високосный")

