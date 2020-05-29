pos = -1


def search(list, a):
    for i in range(len(list)):
        if list[i] == a:
            globals()['pos'] = i
            return True
    return False


lst = [22, 65, 17, 85, 53, 45]
n = 45
if search(lst, n):
    print("Found at", pos)
else:
    print("Not found")