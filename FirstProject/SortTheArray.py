from array import *
arr = array('i', [6, 8, 2, 3, 1])

print("Elements of Original array")
for ele in arr:
    print(ele, end=' ')

print()

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print("Elements of array sorted in ascending order")
for ele in arr:
    print(ele, end=' ')