a = input("Write something: ")
print("Your text:", a)
b = 'h'
index = 0

firstIndex = a.find(b, index, len(a))
lastIndex = a.rfind(b, index, len(a))

strToReplace = a[firstIndex+1:lastIndex].replace(b, b.upper())
a = a.replace(a[firstIndex+1:lastIndex],strToReplace)
print("Your text with replace: ", a)