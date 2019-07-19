a = input()

res = (a.upper().count('G') + a.upper().count('C')) / len(a) * 100
print(res)