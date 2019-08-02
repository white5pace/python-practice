lst = [1, 2, 3, 4, 5, 6]
def modify_list(l):
    x = 0
    firstlen = len(l)
    while x < firstlen:
        if l[0] % 2 != 0:
            l.remove(l[0])
        else:
            l.append(l[0] // 2)
            l.remove(l[0])
        x += 1

print(modify_list(lst))
print(lst)