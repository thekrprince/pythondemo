pos = -1


def search(list, num):
    l = 0
    u = len(list)

    while l <= u:
        mid = (l+u) // 2
        if list[mid] == num:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < num:
                l = mid + 1
            else:
                u = mid - 1
    return False


lst = [15, 28, 38, 47, 59, 61, 78, 85, 99, 111, 135, 148, 205, 258, 272]
n = 111

if search(lst, n):
    print("Found at", pos)
else:
    print("Not Found")