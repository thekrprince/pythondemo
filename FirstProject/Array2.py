from array import *

arr = array('i', [])

size = int(input("Enter the size of array: "))

for i in range(size):
    x = int(input("Enter the next value: "))
    arr.append(x)

print("Original array: {}".format(arr))

start, end = 0, size-1

while start<end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print("Reversed array : {}".format(arr))