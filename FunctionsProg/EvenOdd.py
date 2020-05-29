
def count(a):

    e = 0
    o = 0

    for ele in a:
        if ele%2 == 0:
            e += 1
        else:
            o += 1
    return e, o


lst = [11, 16, 14, 28, 39, 76, 7]
even, odd = count(lst)

print("Count of Even num is {} and Odd num is {} ".format(even, odd))