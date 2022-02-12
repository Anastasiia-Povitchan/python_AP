import math

a = int(input("Введите значение стороны квадрата: "))

def square(a):
    p = 4 * a
    s = a ** 2
    d = a * math.sqrt(2)
    return {"Периметр квадрата": p, "Площадь квадрата": s, "Диагональ квадрата": d}

print(square(a))
