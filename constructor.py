class Animal:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.type = args[1]
        elif len(args) == 3:
            self.name = args[0]
            self.type = args[1]
            self.age = args[2]


class Animal1:
    def __init__(self, **kwargs):
        self.age = None
        self.name = None
        for key, value in kwargs.items():
            setattr(self, key, value)


# list comprehension

lists = []

for i in range(0, 10):
    lists.append(i)
# print(lists)


l1 = [1, 2, 3, 4, 5, 6]
l2 = []

for i in l1:
    l2.append(i ** 2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list comprehension
square_number = [i ** 2 for i in numbers]
even_number = [n for n in numbers if n % 2 == 0]
print(even_number)
# flattening a list of lists: 2 for loops
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_list = [item for sublist in list1 for item in sublist]

word = ["apple", "banana", "cherry", "date"]

first_letter = [i for i in word for i in i[0]]
x = [i[0] for i in word]
square_even_num = [n ** 2 for n in numbers if n % 2 == 0]
# generating a list of the fibonacci sequence using a list comprehension
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

fib_series = [fib[i - 1] + fib[i - 2] for i in range(2, len(fib))]
numbers = 20
count=0
prime_number = [i for i in range(1, 10) if numbers % 2 == 0 ]
print(prime_number)
print(fib_series)
