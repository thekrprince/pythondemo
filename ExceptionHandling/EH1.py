
try:
    a = int(input("Enter Numerator:"))
    b = int(input("Enter Denominator:"))
    print(a/b)
except Exception:
    print("Can't divide by zero")