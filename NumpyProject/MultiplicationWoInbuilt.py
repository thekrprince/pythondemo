from numpy import *

arr1 = array([
                [7, 3, 2],
                [5, 6, 4],
                [9, 1, 1]
            ])

arr2 = array([
                [2, 1, 5],
                [0, 3, 1],
                [1, 3, 4]
            ])

my_list = []

for row in range(len(arr1)):
    temp_arr = []
    for i in range(len(arr1)):
        temp = 0
        for col in range(len(arr2)):
            temp = temp + (arr1[row][col] * arr2[col][i])

        temp_arr.append(temp)
    my_list.append(temp_arr)

for row in my_list:
    print(row)