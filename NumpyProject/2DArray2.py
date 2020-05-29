from numpy import *

arr = array([
                [11, 22, 33, 66, 77, 88],
                [12, 23, 34, 56, 67, 89]
            ])

print("Array 1:")
print(arr)

arr2 = arr.reshape(3, 4)

print("Array 2:")
print(arr2)