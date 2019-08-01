s = 0
sq = 0
while True:
    a = int(input())
    s += a
    sq += a * a
    if s == 0:
        break
print(sq)