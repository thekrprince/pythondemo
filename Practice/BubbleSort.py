

def sort(list):

    for i in range(len(list)):
        for j in range(len(lst)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


lst = [76, 43, 11, 14, 24, 19, 28, 8]
sort(lst)
print(lst)
