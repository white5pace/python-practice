a, b, c = int(input()), int(input()), int(input())

if a >= b:
    Max, Min, Other = a, b, c
else:
    Min, Max, Other = a, b, c

if c >= Max:
    Other, Max = Max, c
elif c <= Min:
    Other, Min = Min, c

print(Max, Min, Other, sep="\n")