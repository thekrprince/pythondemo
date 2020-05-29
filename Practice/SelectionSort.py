
def sort(list):

    for i in range(len(list)):
        min_ind = i
        for j in range(i, len(list)):
            if list[min_ind] > list[j]:
                min_ind = j

        temp = list[min_ind]
        list[min_ind] = list[i]
        list[i] = temp


lst = [67, 54, 11, 8, 85, 29, 44]

sort(lst)
print(lst)