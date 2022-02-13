_month = int(input("Введите номер месяца от 1 до 12: "))

def season(month):

    if month == 12 or 1 <= month < 3:
        return "Зима"
    elif 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    return ("Введите правильное число!")

print(season(_month))