a = input("Введите строку:")
b = input("Введите символ для поиска: ")
print('Ввод закончен. Ищем...')
index = 0
count = 0

while True:
    index = a.find(b, index, len(a))
    if index == -1:
        if count == 0:
            print("Индекс не найдено!")
        break
    print("Индекс символа:", index)
    index += 1
    count += 1