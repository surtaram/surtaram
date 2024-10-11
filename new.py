# second largest element in list

list1 = [2, 3, 4, 33, 4, 3, 45, 55, 32, 344]

# list1.sort(reverse=True)
# print(list1[1])

largest = second_largest = float('-inf')
for i in list1:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print(second_largest)

####
strings = "my name is Pratima"
# reversed_s = ''
# for char in strings:
#     reversed_s = char + reversed_s
# if reversed_s == strings:
#     print("Given string is palindrom")
# else:
#     print("Given string is not palindrome")
# print(reversed_s)

# a=strings.split()
# print(a)
# b=" ".join(reversed(a))
# print(b)

# Duplicate Elements in an Array:-
array = [1, 2, 3, 4, 2, 3, 5, 6, 7, 8, 5]
count = {}
for i in array:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print("Duplicate elements in the array:")
for i, count in count.items():
    if count > 1:
        print(i)




