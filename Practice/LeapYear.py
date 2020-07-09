
def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap

        else:
            leap = True

    return leap


year = is_leap(int(input("Enter a year: ")))
print(year)