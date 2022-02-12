import math

a = int(input("Введите значение стороны квадрата: "))

def square(a):
    p = 4 * a
    # return {"Периметр квадрата:", P}
    s = a ** 2
    # return {"Площадь квадрата:", S}
    d = a * math.sqrt(2)
    # return {"Диагональ квадрата:", d}

    return {"Периметр квадрата": p, "Площадь квадрата": s, "Диагональ квадрата": d}

print(square(a))
