h = int(input('Введите значение высоты треугольника: '))
w = (h * 2) - 1

for i in range(h):
    for j in range(w):
        if i + h - 1 >= j >= h - 1 - i:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
