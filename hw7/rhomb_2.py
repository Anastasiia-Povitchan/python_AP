h = int(input('Введите значение высоты ромба: '))
w = h

for i in range(h):
    for j in range(w):
        if w // 2 - i <= j <= w // 2 + i and i <= h // 2 or j == i - h // 2 or j == h - i + h // 2 - 1 or j == h // 2:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
