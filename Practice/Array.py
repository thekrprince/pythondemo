from array import *

arr = array('i', [33, 12, 15, 48, 75, 2, 22])

print(arr)

print("First Element:", arr[0])
print("Second Element:", arr[1])

for ele in arr:
    print(ele)


# Sorting the Array
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]


print(arr)