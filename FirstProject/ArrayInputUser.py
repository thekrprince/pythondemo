from array import *

arr = array('i', [])

size = int(input("Enter the size of Array: "))

for i in range(size):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)

search = int(input("Enter the value to search: "))

k = 0
for ele in arr:
    if search == ele:
        print(k)
        break

    k+=1