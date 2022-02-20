text = input("Введите текст: ").split()
word = {}

for i in text:
    word[i] = word.get(i, 0) + 1

m = max(word.values())

s = 0

for w in word:
    if word[w] == m:
        # print(word)
        s = w

print("Слово, которое в этом тексте встречается чаще всего - ", s)












