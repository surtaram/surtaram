class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)


class Shape:
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Circle(Shape):
    def draw(self):
        print("Drawing a cricle")


class Square(Shape):
    def draw(self):
        print("Drawing a square")


class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")


def draw_shape(shape):
    shape.draw()


circle = Circle()
square = Square()
rectangle = Rectangle()
draw_shape(circle)
draw_shape(square)
draw_shape(rectangle)
