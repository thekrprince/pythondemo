pos = -1


def search(lst1, a):
    i = 0
    while i < len(lst1):
        if lst[i] == a:
            global pos
            pos = i
            return True
        i += 1
    return False


lst = [3, 8, 12, 7, 5, 25]
n = 25

if search(lst, n):
    print("Found at", pos)
else:
    print("Not found")