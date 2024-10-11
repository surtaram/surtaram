# find sum of an element in the list

my_list = [2, 3, 42, 4, 56, 64]
sum = 0
for i in my_list:
    sum = sum + i

# print(sum)

# multiply total list element
mult = 1
for i in my_list:
    mult = mult * i

# print(mult)

# find smallest and largest number in the list

my_ele=my_list[0]
my_list[0]=max

for i in range(len(my_list)):
    if my_list[i]>max:
        print(i)



