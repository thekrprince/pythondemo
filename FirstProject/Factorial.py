def factorial():
    """
    This functions returns the factorial
    :return:
    """
    num = int(input("Enter a number to get factorial: "))
    for ele in range(1, num):
        num = num * ele
    print(num)

factorial()
