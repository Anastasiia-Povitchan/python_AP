N = int(input("Введите натуральное число: "))
k = 0
i = 1
while i < N:
    i *= 2
    k += 1
    if i*2 > N:
        break
print("Показатель степени:", k, "\n2 ^", k, "=", i)