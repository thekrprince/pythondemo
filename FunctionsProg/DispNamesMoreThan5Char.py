lst = []


def dispname():
    size = int(input("Enter the size of list: "))

    for i in range(size):
        name = input("Enter the {} name: ".format(i))
        lst.append(name)

    print(lst)

    for ele in lst:
        if len(ele) > 5:
            print(ele)
        else:
            pass


dispname()