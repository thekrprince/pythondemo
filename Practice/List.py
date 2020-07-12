lst = [12, "Prince", 167, 65, 23]

print(type(lst))
print(lst)

# Iteration
for ele in lst:
    print(ele)

# Adding the element
lst.append(55)
print(lst)

# Slicing
print(lst[1:4])
# Reverse
print(lst[::-1])

# Updating list values
lst[2] = "Engineer"
print(lst)

# Adding multiple element
lst[3:5] = [111, 222]
print(lst)

# Repetition
print(lst*2)

# Concatenation
lst1 = ['Love', 'Hate']
lst2 = lst + lst1
print(lst2)

# Membership
print(12 in lst)
print('Engineer' in lst2)
print(88 in lst1)

# length
print(len(lst))
print(len(lst1))
print(len(lst2))

# Adding elements to the list
n = int(input('Enter the length to add element in list: '))

for i in range(n):
    lst.append(int(input('Enter the element: ')))

print(lst)

# Removing elements from the list
lst.remove('Engineer')
del lst[1]
print(lst)