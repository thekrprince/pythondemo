# Creating the Dictionary

Myself = {"Name": "Prince", "Job": "Engineer", "Age": 24, "Place": "Bangalore"}

print(type(Myself))
print(Myself)
print("Name :", Myself["Name"])
print("Job :", Myself["Job"])

# Empty Dictionary and then add element one by one
Payal = {}
print(Payal)
Payal['Nickname'] = ('Oli', 'Radha', 'Puja')
Payal['Age'] = 25
Payal['Job'] = 'Developer'
Payal['Place'] = 'Kolkata'

print(Payal)

# Update existing Key's Value
Payal['Place'] = 'Bangalore'
print(Payal)

# Add some more values
Payal['Laptop'] = 'Lenovo'
Payal['Mobile'] = 'Redmi'
Payal['Eyes'] = 'Wear Specs'
Payal['FavColour'] = ['Blue', 'Black', 'Red']
print(Payal)

# Deleted element
del Payal['Eyes']
print(Payal)

# for loop to iterate the keys of the dictionary
for key in Payal:
    print(key)

# for loop to iterate the values of the dictionary
for val in Payal:
    print(Payal[val])