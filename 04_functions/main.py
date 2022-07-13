def greet(first_name, last_name):
    # F here (we can write it in lowercase or uppercase) stands for Formatted. We use it to output a formatted string
    print(F"Hi {first_name} {last_name},")
    print("Welcome aboard")

# Types of functions
# 1. Perform a task
# 2. Return a value


# def greeting(name):
#     print(f"Hi {name}")


# def get_greeting(name):
#     return f"Hi {name}"


# greet("Ahmed", "Ali")
# greeting("John Smith")

# message = get_greeting("Sami Saleem")

# file = open("content.txt", "w")
# file.write(message)

# Parameter VS. Arguments
# Parameter is the input that we write in the function creation
# Argument is the value that we write when we called the function


def add(n1, n2):  # Parameters
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def mod(n1, n2):
    return n1 % n2


# print(add(5, 6))  # Arguments
# print(sub(5, 6))
# print(mul(5, 6))
# print(div(5, 6))
# print(mod(5, 6))


# keyword arguments (keyword= argument)
# default values (optional parameters) [parameter = default value]
def increment(number, by=1):
    return number + by


# print(increment(6))
# print(increment(6, by=3))


# *numbers it is like vararg in Kotlin programming language
# We use it when we want to input multiple variables
# use square brackets [] to create lists and parentheses () to create tuples
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


# print("Start")
# print(multiply(1, 2, 3, 4, 5))

# xargs vs. xxargs
# xargs: variable number of arguments. => lists & tuples
# xxargs: double variable number of arguments. => dict


def save_user(**user):
    print(user)
    print(user["id"])


# save_user(id=0, username="motasem_abunema",
#           display_name="Motasem Abu Nema", age=22, graduated=False, gpa=85.7)

# Scope (Local VS. Global)
message = "Something went wrong"  # Global


def foo(name):
    global message  # Bad practice
    message = f"Hi {name}"  # Local
    print(message)


# print(message)
# foo("Ahmed")


# Exercise fizz_buzz algorithm

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return"Buzz"
    return input


print(fizz_buzz(7))
