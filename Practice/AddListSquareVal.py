N = int(input())

# Get the input
numArray = map(int, input().split())

sum_integer = 0
# Write the logic to add these numbers here
num = list(numArray)
sqr = []

for i in range(N):
    temp = num[i] ** 2
    sqr.append(temp)

print(sqr)

for i in range(N-1):
    sqr[i+1] = sqr[i] + sqr[i+1]
    sum_integer = sqr[i+1]


# Print the sum
print(sum_integer)