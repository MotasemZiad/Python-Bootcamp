from math import *
print("Hello World!")
print("*" * 10)

name = "Motasem"
age = 22

print(f"My name is {name} I'm {age} years old")

x = 1
y = 1
unit_price = 3


# Comments
# Hello This is a single line comment in python
"""
Unfortunately, this is a string with no effect, not a multi-line comment
because python doesn't support multi-line comment.
"""


students_count = 1000  # integer (real number)
rating = 4.99  # float (floating-point number)
is_published = False  # boolean (case-sensitive True or False)
course_name = "Python Programming"  # string (sequence of characters)
print(
    f"Course Name: {course_name}\nStudents Count: {students_count}\nRating: {rating}\nPublished: {is_published}")

# All variables' names are descriptive and meaningful
# We used lowercase letters to name our variables (snake_case) neither camelCase nor PascalCase


# Types of strings
single_quote = 'Hello, This is Motasem'
double_quote = "Hi there, I hope you are doing well"
triple_quote = """
    Hi John, I hope you had a great weekend
    This is Motasem from motasemziad.github.io/Personal-Website
    Blah, blah, blah

    Yours sincerely
    Motasem
"""
print(single_quote + "\n" + double_quote + "\n" + triple_quote)

# String
course = "  Python Programming  "
print(len(course))
print(course[0])
print(course[-1])
print(course[0:2])  # last index is excluded
print(course[0:])
print(course[:2])  # it starts from ZERO by default
print(course[:])

# Skip sequences in String
# \"
# \'
# \\
# \n
# \t
print("Python \"Programming")
print('Python \'Programming')
print("Python \\Programming")
print('Python \nProgramming')
print('Python \tProgramming')
print('Python \rProgramming')

first_name = "Motasem"
last_name = "Abu Nema"
full_name = first_name + " " + last_name
full_name2 = F"{first_name} {last_name}"
full_name_length = f"{len(first_name)} {len(last_name)}"
print(full_name)
print(full_name2)
print(full_name_length)

# String methods
print(course.upper())
print(course.lower())
print(course.capitalize())
print(course.title())
print(course.strip())  # strip is like the trim() method in other programming languages which is used to remove all the whitespaces from left or right of the string
print(course.find('ro'))
print(course.replace("P", "J"))
# casefold() method is used to make the string case-insensitive
print("pro" in course.casefold())  # return a boolean type
print("swift" not in course)  # the same thing as the above example

# Numbers methods
print(round(2.9))
print(trunc(2.9))
print(abs(-19))
print(sqrt(64))
print(pow(9, 2))
print(floor(2.3))
print(ceil(2.3))

# Input "Type Conversion"
int(x)
float(x)
bool(x)
str(x)
x = int(input("x: \n"))
print(type(x))
y = x + 1
print(f"x: {x}, y: {y}")

# Falsy values in python
# "" empty string
# 0
# None => Represents the absence of a value
print(bool("False"))
