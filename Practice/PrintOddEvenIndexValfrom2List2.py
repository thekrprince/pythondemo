lst1 = [10, 13, 6, 22, 27, 19, 8, 15]
lst2 = [5, 99, 76, 43, 11, 21, 38, 56]

lst3 = []

odd = lst1[1::2]
print("Element at odd-index positions from list one")
print(odd)

even = lst2[0::2]
print("Element at even-index positions from list two")
print(even)

lst3.extend(odd)
lst3.extend(even)

print("Printing Final third list")
print(lst3)