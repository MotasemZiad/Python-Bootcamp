# Object Oriented Programming
# Class: a blueprint for creating new objects
# Object: an instance of a class
# Magic Methods: __sth__()
# Each class has attributes & properties
# Class Attributes VS. Instance Attributes
# Class Methods VS. Instance Methods
# In general class attributes and methods are static typed in other programming languages

# class Point:
#     default_color = "Red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point({self.x}, {self.y})")


# point = Point(x=17, y=18)
# another = Point(7, 8)
# print(point == another)
# print(point > another)
# print(point + another)


# print(point.__str__())
# point.draw()
# another.draw()
# print("Type of Point class: ", type(point))
# print("Is instance? ", isinstance(point, Point))


# # We can access attributes by class, or by instance
# # It act exactly like the static attributes
# Point.default_color = "Blue"
# print(Point.default_color)
# print(point.default_color)
# print(another.default_color)


# # Factory method
# point = Point(0, 0)
# point.draw()

# Private & Protected Attributes
# Private Attributes with double underscore __private
# Protected Attributes with single underscore _protected

# Making Custom Containers
# class TagCloud:

#     def __init__(self):
#         self.__tags = {}

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1


# cloud = TagCloud()

# cloud.add("python")
# cloud.add("Python")
# cloud.add("python")

# cloud.__setitem__("java", 2)

# print(cloud.__len__())

# print(list(cloud.__iter__()))
# print(cloud.__getitem__("PYTHON"))
# print(cloud.__dict__)

# Getters and Setters

# class Product:

#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, price):
#         if(price > 0):
#             self.__price = price
#         else:
#             raise ValueError("Price cannot be negative.")


# product1 = Product(50)
# product1.price = 7
# print(product1.price)

# Inheritance
# DRY -> Don't Repeat Yourself
# The parent class of all classes in python called: object

# Animal: Parent, Base, Super class
# Mammal: Child, Derived, Sub class
# class Animal(object):

#     def __init__(self):
#         print("Animal Constructor")
#         self.age = 1

#     def eat(self):
#         print("Eat")


# class Mammal(Animal):
#     def __init__(self):
#         print("Mammal Constructor")
#         self.weight = 2
#         super().__init__()

#     def walk(self):
#         print("Walk")


# class Fish(Animal):
#     def swim(self):
#         print("Swim")


# m = Mammal()
# print(m.age)
# print(m.weight)

# m.eat()
# m.walk()
# print(m.age)

# f.eat()
# f.swim()
# print(f.age)

# print(isinstance(m, Animal))
# print(isinstance(f, object))
# print("Is subclass: ", issubclass(Mammal, Animal))

# Method Overriding
# Method Overloading

# Multi-level Inheritance
# class Animal():

#     def eat(self):
#         print("Eat")


# class Bird(Animal):
#     def fly(self):
#         print("Fly")


# class Chicken(Bird):
#     pass

# Multiple Inheritance
# A class that can be a child of two parents which doesn't make any sense, but still it is a feature in Python
# it is a feature in Python and C++ programming languages

# class Employee:

#     def greet(self):
#         print("Employee Greet")


# class Person:

#     def greet(self):
#         print("Person Greet")


# class Manager(Person, Employee):
#     pass


# # m = Manager()

# # m.greet()
# # m.greet()


# class Flyer:
#     def fly(self):
#         print("Flying..")


# class Swimmer:
#     def swim(self):
#         print("Swimming..")


# class FlyingFish(Flyer, Swimmer):
#     pass


# flying_fish = FlyingFish()
# flying_fish.fly()
# flying_fish.swim()

# A good example of Inheritance

# from abc import ABC, abstractmethod


# class InvalidOperationError(Exception):
#     pass


# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("The stream is already opened")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("The stream is already closed")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):

#     def read(self):
#         print("Reading data from a file")


# class NetworkStream(Stream):

#     def read(self):
#         print("Reading data from a network")


# class MemoryStream(Stream):

#     def read(self):
#         print("Reading data from a memory")

# Polymorphism
# Poly -> many, morphism -> forms = many forms
# from abc import ABC, abstractmethod

# Duck Typing
# Python is a dynamically typed programming language which means it
# doesn't care of the type of a parameter if it has the methods
# and functionality that can't raise an error
# class TextBox:
#     def draw(self):
#         print("TextBox")


# class DropDownList:
#     def draw(self):
#         print("DropDownList")


# def draw(controls):
#     for control in controls:
#         control.draw()


# ddl = DropDownList()
# tb = TextBox()

# draw([tb, ddl])


# Extending Built-in Types
# class Text(str):
#     def duplicate(self):
#         return self + self


# txt = Text("Python")
# print(txt.duplicate())


# class TrackableList(list):
#     def append(self, element):
#         print(f"{element} Appended")
#         super().append(element)


# list1 = TrackableList()

# list1.append("Swimming")
# list1.append("Listening")
# list1.append("Reading")
# list1.append("Writing")

# print(list1)

# Data classes (Named Tuples)
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# p1 = Point(7, 8)
# p2 = Point(x=7, y=8)

# print(p1 == p2)
# print("id of p1: ", id(p1))
# print("id of p2: ", id(p2))

# from collections import namedtuple

# Point = namedtuple("Point", ["x", "y"])
# p1 = Point(x=1, y=2)
# p2 = Point(1, 2)
# p3 = Point(x=12, y=24)
# print(p1 == p2)
# print(p1)
# print(p2)


# User = namedtuple("User", ["username", "display_name", "email", "phone"])

# ahmed = User(username="ahmed_ali", display_name="Ahmed Ali",
#              email="ahmed@gmail.com", phone="0599838232")
# khalid = User(username="khalid_ali", display_name="Khalid Ali",
#               email="khalid@gmail.com", phone="0599838999")
# print(ahmed == khalid)
# print(ahmed)
# print(khalid)
