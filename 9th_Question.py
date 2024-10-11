# How to remove Nth occurrence of the word from a list
arr = ['best', 'of', 'of', 'Yesh', 'Yesh']

count = 0
inp = input("Enter the world:")

for i in arr:
    if i == inp:
        count = count + 1
        if count == 2:
            arr.remove(i)

print(arr)
