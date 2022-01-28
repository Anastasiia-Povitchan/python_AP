N = int(input("Введите целое число: "))
for kv in range (1, N):
    if (kv**2) > N:
        break
    print(kv ** 2, end='; ')

