from array import *

arr = array('i', [])

size = int(input("Enter the size of an Array: "))

for i in range(5):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)

for j in range(size):
    if(j==1):
        pass
    else:
        print(arr[j])