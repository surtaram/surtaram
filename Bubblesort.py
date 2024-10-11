arrays = [3, 4, 2, 6, 4, 7, 5, 9, 8]

for i in range(0, len(arrays) - 1):
    for j in range(len(arrays) - 1):
        if arrays[j] > arrays[j + 1]:
            temp = arrays[j]
            arrays[j] = arrays[j + 1]
            arrays[j + 1] = temp

print(arrays)

# insertion
arrays = [3, 4, 2, 6, 4, 7, 5, 9, 8]
n = len(arrays)

for i in range(1, n):
    j = i - 1
    key = arrays[i]
    while j >= 0 and key < arrays[j]:
        arrays[j + 1] = arrays[j]
        j -= 1
        arrays[j + 1] = key

print(arrays)

# selection


arrays = [3, 4, 2, 6, 4, 7, 5, 9, 8]
