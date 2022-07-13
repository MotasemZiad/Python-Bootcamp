# How to name things

# 1. Meaningful names
d = 19  # elapsed time in days # Bad
elapsed_time_in_days = 19  # Good

# 2. Avoid Disinformation
account_list = []  # Bad
accounts = []  # Good

# 3. Avoid Noise Words (The, info, data, variable, object, manager)
user_info = {"key": "value"}  # Bad
customer_data = {"key": "value"}  # Bad

user = {"key": "value"}  # Good
customer = {"key": "value"}  # Good

# 4. Use Pronounceable Names
yyyymmdstr = "YYYY/MM/DD"  # Bad
current_date = "YYYY/MM/DD"  # Good

# 5. Avoid using Magic Numbers. Use Searchable Names
salary = 5000
if(salary > 3000):
    print("Do something")
else:
    print("Do something else")  # Bad

MINIMUM_SALARY = 3000
if(salary > MINIMUM_SALARY):
    print("Do something")
else:
    print("Do something else")  # Good

# 6. Be Consistent: one word for each concept
# for instance: don't use fetch, retrieve, and get for the same operations in the same project.
# choose one and use it all over the project.

# How to write functions

# 1. Keep them small


def get_users():
    print("Do just one thing")

# 2. Make Sure They Just Do One Thing (SOLID principles first one => Single Responsibility)
# if you find a long function you should extract other functions from it.

# 3. Encapsulate Conditionals in Functions
# Use functions like: is_valid_insertion() instead of multi conditions like this:
# column <= NUM_COLUMNS and column >= 1 and numberOfItemsInColumn[column - 1] < NUM_ROWS and getWinner() != Chip.NONE


def is_authorize() -> bool:
    print("Check whether the user is authorize or not")

# 4. Fewer Arguments
# Functions should have two or fewer arguments, the fewer the better.
# Avoid three or more arguments where possible.


def register(id, username, email, password, phone, bio, image):
    print("Register Functionality")  # Bad


def registration(user):
    print("User Functionality")  # Good

# 5. Do not use Flag Arguments.
# instead divide the function into two functions


def book(customer_name, is_premium=False):
    if(is_premium):
        print("Logic for premium book")
    else:
        print("Logic for freemium book")  # Bad


def premium_book(customer_name):
    print("Logic for premium book")


def freemium_book(customer_name):
    print("Logic for freemium book")  # Good

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
