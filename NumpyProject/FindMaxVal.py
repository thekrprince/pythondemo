from numpy import  *

arr = array([33, 22, 46, 19, 34])
maxm = 0
for i in range(len(arr)):
    if arr[i] > maxm:
        maxm = arr[i]
    else:
        pass

print(maxm)