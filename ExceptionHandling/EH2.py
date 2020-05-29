try:
    a = float(input("Enter numerator:"))
    b = float(input("Enter Denominator:"))
    c = a/b
    print(c)
except Exception:
    print("Can't divide by zero")
else:
    print("Else block")