try:
    print("Resource open")
    a = int(input("Enter a number to divide:"))
    b = int(input("Enter 2nd number:"))
    c = a/b
    print(c)

except (ZeroDivisionError, ValueError):
    print("Invalid Input, can't divide")

else:
    print("Resource closed")