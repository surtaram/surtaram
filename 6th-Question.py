# find maximum and minimum value in the array

array = [1, 2, 34, 53, 56, 22, 456, 567]
# maximum value
max = array[0]
n = len(array)

for i in range(1, n):
    if array[i] > max:
        max = array[i]

print("maximum value in the array: ", max)

# mimimum value

min = array[0]
n = len(array)
for i in range(1, n):
    if array[i] < min:
        min = array[i]

print("mimimum value in the array: ", min)
