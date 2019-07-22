a = input()
counter = 1
letter = a[0]
res = ''
for i in range(1, len(a)):
    if a[i] != letter:
        res += letter + str(counter)
        counter = 1
        letter = a[i]
    else:
        counter += 1
res += letter + str(counter)
print(res)
