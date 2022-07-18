# Exceptions in Python

# numbers = [1, 2]
# print(numbers[3])

# Handling Exceptions
# try except block, try except else block, try except finally block

# Context Management Protocol
# When an object has these two methods __enter__(), __exit__()

# try:
#     with open('03_control_flow/main.py', encoding="utf-8") as file:
#         print("File opened")
#         file.__enter__()
#         file.__exit__()
#     age = int(input("Age: "))
#     print(f"Your age is: {age}")
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) as e:
#     print("You didn't enter a valid age.")
#     print(e)
#     print(type(e))
# else:
#     print("No exceptions were thrown.")

# print("Execution Continues...")


# Raising an exception (throwing an exception)

from timeit import timeit
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
try:
    xfactor = 10 / 0
except ZeroDivisionError as e:
    pass
"""


print("First code", timeit(code1, number=10000))
print("***************************")
print("Second code", timeit(code2, number=10000))
