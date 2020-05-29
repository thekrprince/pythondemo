size = int(input("Enter the size: "))
rng = int(input("Enter the range of number: "))


def fibonacci(s, r):
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
            a = b
            b = c

            if c < r:
                print(c)
            else:
                break


fibonacci(size, rng)