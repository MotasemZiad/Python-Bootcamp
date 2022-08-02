# # How to name things

# # 1. Meaningful names
# d = 19  # elapsed time in days # Bad
# elapsed_time_in_days = 19  # Good

# # 2. Avoid Disinformation
# account_list = []  # Bad
# accounts = []  # Good

# # 3. Avoid Noise Words (The, info, data, variable, object, manager)
# user_info = {"key": "value"}  # Bad
# customer_data = {"key": "value"}  # Bad

# user = {"key": "value"}  # Good
# customer = {"key": "value"}  # Good

# # 4. Use Pronounceable Names
# yyyymmdstr = "YYYY/MM/DD"  # Bad
# current_date = "YYYY/MM/DD"  # Good

# # 5. Avoid using Magic Numbers. Use Searchable Names
# salary = 5000
# if(salary > 3000):
#     print("Do something")
# else:
#     print("Do something else")  # Bad

# MINIMUM_SALARY = 3000
# if(salary > MINIMUM_SALARY):
#     print("Do something")
# else:
#     print("Do something else")  # Good

# # 6. Be Consistent: one word for each concept
# # for instance: don't use fetch, retrieve, and get for the same operations in the same project.
# # choose one and use it all over the project.

# # How to write functions

# # 1. Keep them small


# def get_users():
#     print("Do just one thing")

# # 2. Make Sure They Just Do One Thing (SOLID principles first one => Single Responsibility)
# # if you find a long function you should extract other functions from it.

# # 3. Encapsulate Conditionals in Functions
# # Use functions like: is_valid_insertion() instead of multi conditions like this:
# # column <= NUM_COLUMNS and column >= 1 and numberOfItemsInColumn[column - 1] < NUM_ROWS and getWinner() != Chip.NONE


# def is_authorize() -> bool:
#     print("Check whether the user is authorize or not")

# # 4. Fewer Arguments
# # Functions should have two or fewer arguments, the fewer the better.
# # Avoid three or more arguments where possible.


# def register(id, username, email, password, phone, bio, image):
#     print("Register Functionality")  # Bad


# def registration(user):
#     print("User Functionality")  # Good

# # 5. Do not use Flag Arguments.
# # instead divide the function into two functions


# def book(customer_name, is_premium=False):
#     if(is_premium):
#         print(f"Logic for premium book {customer_name}")
#     else:
#         print(f"Logic for freemium book {customer_name}")  # Bad


# def premium_book(customer_name):
#     print(f"Logic for premium book {customer_name}")


# def freemium_book(customer_name):
#     print(f"Logic for freemium book {customer_name}")  # Good

# 6. Do Not Have Side Effects
# If your function do more than one thing extract it to two function

# 7. Don't Repeat Yourself (DRY)
# If you see a repeated code wrap it inside a function and use it instead.
# Write once, use everywhere

# Do not leave code in comments
# Just delete the code even if it is important there are cool thing called Version Control
# and you can find the code whenever you want.

# Know your language's conventions
# Know your language name conventions. It is important to write consistent code.

# https://www.youtube.com/watch?v=8OKTAedgFYg
# 11 tips and tricks to write better Python Code
# All tips
# 1) Iterate with enumerate instead or range(len(x))
# 2) Use list comprehension instead of raw for loops
# 3) Sort complex iterables with sorted()
# 4) Store unique values with Sets
# 5) Save memory with Generators
# 6) Define default values in Dictionaries with .get() and .setdefault()
# 7) Count hashable objects with collections.Counter
# 8) Format strings with f-Strings (Python 3.6+)
# 9) Concatenate strings with .join()
# 10) Merge dictionaries with {**d1, **d2} (Python 3.5+)
# 11) Simplify if-statements with if x in list


# print([i*i for i in range(10)])
# print([i*-1 for i in range(-50, 50) if i < 0])

# data = [1, 5, 2, 10, 8, 6]
# sorted_data = sorted(data)
# print(sorted_data)

# my_dict = {"item": "Football", "price": 12.99}
# count = my_dict.get("count", 0)
# print(count)

# my_dict.setdefault("count", 0)
# print(my_dict)

# from collections import Counter

# my_list = [10, 10, 10, 9, 9, 5, 5, 9, 9, 10, 10, 11, 12, 11, 11, 5]

# counter = Counter(my_list)
# print(counter.most_common(2))
# print(counter)

# Dataclasses in Python
# import string
# import random
# from dataclasses import dataclass, field


# def generate_id() -> str:
#     return "".join(random.choices(string.ascii_letters + string.digits, k=12))


# @dataclass(frozen=True, kw_only=True, slots=True)
# class Person():
#     id: str = field(init=False, default_factory=generate_id)
#     name: str
#     address: str
#     active: bool = True
#     email_addresses: list[str] = field(default_factory=list)


# def main():
#     person = Person(name="John Doe", address="132 Main St.")
#     print(person)


# if __name__ == "__main__":
#     main()
