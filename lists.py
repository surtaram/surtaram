L1 = [1, 2, 0, 5, 0, 0, 15, 0]


# for i in range(0, len(L1) - 1):
#     for j in range(len(L1) - 1):
#         if L1[j] > L1[j + 1]:
#             temp = L1[j]
#             L1[j] = L1[j + 1]
#             L1[j + 1] = temp

def move_zeros(input):
    position = 0
    for j in range(len(L1)):
        if input[j] != 0:
            input[position], input[j] = input[j], L1[position]

            position = position + 1
    return input


print(move_zeros(L1))




lst=[1,2,3,4,5,6,7]
lst1=[]
for i in lst:
    lst1.append((i**2))

print(lst1)

num=[[1,2,3],[4,5,6],[7,8,9]]


new_list=[item for sublist in num for item in sublist]

print(new_list)
l1=[]
for item in num:
    for j in item:
        l1.append(j)
print(l1)

square=[i**2 for i in l1 if i%2==0]
print(square)

words=["apple","banana","cherry"]

first_letter=[word[0] for word in words]
print(first_letter)



thislist = ["apple", "banana", "cherry"]

thislist.clear()
print(thislist)

s = 'abcdddccgg'


def word_order_reverse(input):
    new = input.split()
    output = []
    for char in range(len(new) - 1, -1, -1):
        output.append(new[char])
    reverse_word = " ".join(output)
    return reverse_word


s = 'My name is Surta'
print(word_order_reverse(s))