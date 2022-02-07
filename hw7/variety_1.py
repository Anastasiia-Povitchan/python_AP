from random import randint
a =[(randint(0, 25)) for _ in range(5)]
print("Данные: ", a)
unique_a = set(a)
print("Уникальные данные: ", unique_a)