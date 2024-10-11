# Swap first and last elements in a list

# approach-1 -temp variable
input = [12, 35, 9, 56, 24]


size=len(input)

temp=input[0]

input[0]=input[size-1]
input[size-1]=temp

print(input)
