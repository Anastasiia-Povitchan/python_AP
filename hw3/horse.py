def isValid(coord):
    return len(coord) == 2 and (coord[0] >= 'a' and coord[0] <= 'h') and (coord[1] >= '1' and coord[1] <= '8')

start = input('Введите начальное положение коня: ').lower()
if isValid(start):
    print('Продолжаем...')
else:
    print('Нужны корректные координаты: abcdefgh 12345678')
    exit()

finish = input('Введите желаемое положение коня: ').lower()
if isValid(finish):
    print('Конь пошел...')
else:
    print('Нужны корректные координаты: abcdefgh 12345678')
    exit()

# Конь пошел

x1 = ord(start[0])
y1 = int(start[1])

x2 =ord(finish[0])
y2 = int(finish[1])

if abs(x1 -x2) == 1 and abs(y1 - y2) == 2 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
        print("...успешно")
else:
        print("...не пошел")
