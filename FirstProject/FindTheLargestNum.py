num1 = int(input("Enter the 1st Number to compare: "))
num2 = int(input("Enter the 2nd Number to compare: "))
num3 = int(input("Enter the 3rd Number to compare: "))

if (num1 >= num2) and (num1 >= num3):
    print("{} is greater among all the 3 numbers".format(num1))
elif (num2 >= num1) and (num2 >= num3):
    print("{} is greater among all the 3 numbers".format(num2))
else:
    print("{} is greater among all the 3 numbers".format(num3))