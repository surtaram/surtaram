# Abstraction implementation
from abc import ABC, abstractmethod


# abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print("Car engine stated")

    def stop_engine(self):
        print("Car engine stopped")


# concrete class
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

    def stop_engine(self):
        print("Bike engine stopped")


car = Car()
bike = Bike()
car.start_engine()
bike.start_engine()


# Abstraction: User ko bas yeh pata hota hai ki vehicle ka engine
# start ya stop karna
# hai, lekin uska internal mechanism hide kiya gaya hai.

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def deposit(self,amount):
        pass


# concrete class

class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def check_balance(self):
        return f"Balance:{self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount + (amount + self.interest_rate)
            print(f"Deposited:{self.balance}.New balance:{self.balance}")
        else:
            print("Invalid deposite amount")


class CurrentAccount(BankAccount):
    def check_balance(self):
        return f"current account balance:{self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited :{amount},new balance is {self.balance}")
        else:
            print("Invalid deposit amount")


account = SavingsAccount(1000)
account.deposit(900)
print(account.check_balance())


# example 3

# abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# example 4
# abstract class
class Shape1(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimter(self):
        pass


class Rectangle(Shape1):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimter(self):
        return 2 * (self.length + self.width)


class Cicrle1(Shape1):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


rectangle = Rectangle(5, 10)
circle = Circle(7)
