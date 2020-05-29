numArray = map(int, input("Enter some num: ").split())

sum = 0

lst = list(numArray)
print(type(lst))

for i in range(len(lst)-1):
    lst[i+1] = lst[i] + lst[i+1]
    sum = lst[i + 1]

print(sum)