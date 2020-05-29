try:
    print("Resource open")
    a = int(input("Enter numerator to divide:"))
    b = int(input("Enter denominator to divide:"))
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print("Please pass other numeric value than Zero", e)
except ValueError as v:
    print("Please provide valid value", v)
finally:
    print("Resource closed") 