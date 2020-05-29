from numpy import *

arr1 = array([12, 65, 15, 20, 34])
arr2 = array([26, 17, 32, 45, 9])

for i in range(len(arr1)):
    arr1[i] = arr1[i] + arr2[i]
    print(arr1[i])