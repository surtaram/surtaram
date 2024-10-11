# Python Object Oriented Programming

# Inheritance :-

class Car:
    def __init__(self, windows, doors, engine_type):
        self.windows = windows
        self.doors = doors
        self.engine_type = engine_type

    def driving(self):
        print("Car is used for driving")


# Audi car is inheriting from car class
class Audi(Car):
    def __init__(self, windows, doors, engine_type, horsepower):
        super().__init__(windows, doors, engine_type)
        self.horsepower = horsepower

    def driving(self):
        print("It is a self driving car")


audiq7 = Audi(4, 5, "Petrol", 200)
print(audiq7.doors)
print(audiq7.windows)
audiq7.driving()

print(dir(audiq7))  # to print the access of particular object in python


# ['__class__', '__delattr__', '__dict__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getstate__', '__gt__',
# '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__',
# 'doors', 'driving', 'engine_type', 'horsepower',
# 'windows']


# Encapsulation in python

# Encapsulation is a fundamental principle in object oriented programming that
# focuses on bundling data and the methods that operate on that
# data into a single unit called a class.
# It allows you to control the access and visibility of the data
# and methods ,providing a way to protect and organize your code
# Access modifier :-
# Private :- Those method which is only accessible within the classes

class Person:
    # constructor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display_info(self):
        print(f"The person name is {self.__name} and the age is {self.__age}")


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def display_info(self):
        print(f"The person name is {self.__name} and the age is {self.__age}")


person = Person("surta", 27)
person.display_info()
print(dir(person))

