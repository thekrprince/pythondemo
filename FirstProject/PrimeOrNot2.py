import math as m

num = int(input("Enter a number to check whether it's Prime or not: "))

if num == 1:
    print("Not a Prime number")
else:
    sqr = m.floor(m.sqrt(num))
    for i in range(2, sqr+1):
        if(num%i==0):
            print("Not a Prime number, got divided by {}".format(i))
            break
    else:
        print("It's a Prime number")
