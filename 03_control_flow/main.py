# # Comparison Operators
# # > < >= <= == !=

# # Logical Operators
# # And, Or, Xor, and Not

# # Arithmetic Operators
# # + - * / % **

# # Control statements
# # if-else, nested-if-else, Ternary Operator

temperature = 19
if(temperature > 30):
    print("It's warm")
    print("Drink Water")
elif(temperature > 20):
    print("It's nice")
else:
    print("It's cold")
print("Done")

age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

high_income = True
good_credit = True
student = False

if(high_income and good_credit):
    print("Eligible")
else:
    print("Not eligible")

if not student:
    print("Eligible")
else:
    print("Not eligible")

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# In Python Logical operators are short-circuit which it means in the and operator for example if the first argument is false,
# the whole expression considered to be false.

# age should be between 18 and 65
age = 22
if age >= 18 and age < 65:
    print("Qualified")
else:
    print("Not qualified")

if 18 <= age < 65:
    print("Qualified")
else:
    print("Not qualified")

# Loops: while, for, and for-else loops

for i in range(1, 10, 2):
    print(i)

for number in range(3):
    print("Sending a message", number + 1, (number + 1) * ".")

successful = False
for num in range(3):
    print("Attempt #" + str(num + 1))
    if(successful):
        print("Successful")
        break
else:
    print("Something went wrong")

for x in range(10):
    for y in range(5):
        for z in range(3):
            print(f"({x}, {y}, {z})")


print(type(5))
print(type(range(5)))

# Iterables
# range, strings, tuples, lists, and dictionaries...etc
for i in "Python":
    print(i)

for j in [1, 2, 3, 4, 5]:
    print(j)

for k, v in {"name": "Ahmed", "age": 36, "gpa": 86.0, "graduated": False}.items():
    print(f"{k}: {v}")

number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">>")
    print("ECHO", command)

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

# Exercise
count = 0
for i in range(1, 100):
    if(i % 2 == 0):
        count += 1
        print(i)
else:
    print(f"We have {count} even numbers")
