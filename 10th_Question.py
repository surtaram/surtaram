# Count occurrences of an element in a list
my_list = [2, 3, 4, 5, 3, 4, 2, 5, 3]

x = 2

count = 0
for i in my_list:
    if i == 2:
        count = count + 1
    else:
        pass

print(count)
