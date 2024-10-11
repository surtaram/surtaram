class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"{self.brand} has {self.speed} km/h")


class Car(Vehicle):
    def __init__(self, brand, speed, music_system):
        super().__init__(brand, speed)
        self.music_system = music_system

    def play_music(self):
        print(f"{self.brand} has music system")


vehicle = Vehicle("Honda", 80)
vehicle.drive()

car = Car("Maruti", 100, True)
car.play_music()


# Single Inheritance

class Parent:
    def show(self):
        print("This is parent class or base class")


class Child(Parent):
    def display(self):
        print("This is child class methods")


child = Child()
child.show()
child.display()


# Multiple Inheritance

class Father:
    def show_father(self):
        print("This is parent1 class")


class Mother:
    def show_mother(self):
        print("This is parent 2 class")


class Child1(Father, Mother):
    def display(self):
        print("This is child class")


child1 = Child1()
child1.display()
child1.show_mother()
child1.show_father()


# Multilevel Inheritance

class Grandparent:
    def show_grandparent(self):
        print("This is grandparent class")


class Parent1(Grandparent):
    def show_parent1(self):
        print("This is parent1 class")


class Child2(Parent1):
    def show_child2(self):
        print("This is child1 class")


child_o = Child2()
child_o.show_parent1()
child_o.show_grandparent()
child_o.show_child2()


# Hierarchical Inheritance

class Parent2:
    def show(self):
        print("This is parent2 class")


class Child3(Parent2):
    def display3(self):
        print("This is child1 method")


class Child4(Parent2):
    def display4(self):
        print("This is child4 methods")


# Hybrid Inheritance

class Base:
    def show_base(self):
        print("This is base class method")


class Parent12(Base):
    def show_parent12(self):
        print("This is parent12 class method")


class Parent13(Base):
    def show_parent13(self):
        print("This is parent13 class method")


class Child11(Parent13, Parent12):
    def show_child11(self):
        print("This is child class method")
