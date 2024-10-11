#Swap any two elements in a list

my_list=[23,65,19,90]

size=len(my_list)

temp=my_list[0]
my_list[0]=my_list[size-2]
my_list[size-2]=temp

print(my_list)