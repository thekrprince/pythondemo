# Interchanging first and last element of a list
lst = [10, 20, 30, 40, 50]

size = len(lst)

lst[0], lst[size-1] = lst[size-1], lst[0]

print(lst)

# Method 2
def swap(newlist):
    size1 = len(newlist)
    newlist[0], newlist[size1-1] = newlist[size1-1], newlist[0]
    return newlist


lst1 = [55, 64, 111, 245, 888]
swapped = swap(lst1)
print(swapped)