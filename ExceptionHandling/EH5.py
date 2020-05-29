try:
    age = int(input("Enter the age: "))
    if age < 18:
        raise Exception
    else:
        print("Can vote")

except:
    print("Can't vote")