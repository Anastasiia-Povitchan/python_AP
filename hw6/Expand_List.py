import random
rangeStart = int(input("Enter start range: "))
rangeEnd = int(input("Enter end range: "))
if rangeStart >= rangeEnd:
    print("Invalid start/end")
    exit()

size = int(input("Enter range size: "))
if size < 1:
    print("Invalid size")
    exit()

a = random.sample(range(rangeStart, rangeEnd), size)
print("Your string:", a)
for i in range(len(a)//2):
    a[i], a[-i-1] = a[-i-1], a[i]
print("Reverse string:", a)