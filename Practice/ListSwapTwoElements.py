# Given a list in Python and provided the positions of the elements,write a program to swap the two elements in the list


def swap(newlst):
    size = len(newlst)
    i = int(input('Enter the 1st index between 0 to {}: '.format(size)))
    j = int(input('Enter the 2nd index between 0 to {}: '.format(size)))

    if i < size and j < size:
        newlst[i], newlst[j] = newlst[j], newlst[i]
        return newlst
    else:
        print('Please enter the valid index!!!')
        exit()


lst = [11, 22, 33, 44, 55, 66]
swapped = swap(lst)
print(swapped)