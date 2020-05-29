N = int(input())

# Get the input
numArray = map(int, input().split())

sum_integer = 0
# Write the logic to add these numbers here
num = list(numArray)

for i in range(N-1):
    num[i+1] = num[i] + num[i+1]
    sum_integer = num[i+1]


# Print the sum
print(sum_integer)