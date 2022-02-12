_month = int(input("Введите номер месяца от 1 до 12: "))

if _month > 12 or _month == 0:
    print("Введите правильное число!")
    exit()

def season(month):
    if _month == 12 or _month < 3:
        return "Зима"
    elif _month == 3 or _month < 6:
        return "Весна"
    elif _month == 6 or _month < 9:
        return "Лето"
    else:
        return "Осень"

print(season(_month))

