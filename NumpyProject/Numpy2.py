from numpy import  *

arr1 = array([2, 5, 6, 8, 3])

arr2 = arr1.view()

arr2[1] = 13

print(arr1)
print(arr2)