size = int(input("Enter the size: "))


def fibonacci(s):
    a = 0
    b = 1

    if s < 0:
        print("Wrong input")
    elif s == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, s):
            c = a + b
            print(c)
            a = b
            b = c


fibonacci(size)