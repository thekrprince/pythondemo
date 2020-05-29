# 1: Given a two list. Create a third list by picking an odd-index element from the first list and even index elements
# from second.
lst1 = [3, 2, 7, 12, 6, 9, 8]
lst2 = [12, 34, 22, 46, 17, 21, 88]

lst3 = []

for i in range(len(lst1)):
    if i % 2 == 1:
        lst3.append(lst1[i])

for j in range(len(lst2)):
    if j % 2 == 0:
        lst3.append(lst2[j])

print(lst3)
