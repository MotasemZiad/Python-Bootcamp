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

class Product:

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if(price > 0):
            self.__price = price
        else:
            raise ValueError("Price cannot be negative.")


product1 = Product(50)
product1.price = 7
print(product1.price)
