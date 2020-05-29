try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    if b == 0:
        raise ZeroDivisionError
    else:
        print(a/b)
except ZeroDivisionError:
    print("Can't divide by zero")