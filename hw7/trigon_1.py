h = int(input('Введите значение высоты треугольника: '))
w = h * 2 - 1

for i in range(h):
    for j in range(w):
        if j == i + h - 1 or j == h - 1 - i or i == h - 1:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
