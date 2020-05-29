num = int(input("Enter a number: "))

for i in range(2, num+1):
    if num % i == 0:
        break

if i == num:
    print("{} is a prime number".format(num))
else:
    print("{} is not a prime number".format(num))