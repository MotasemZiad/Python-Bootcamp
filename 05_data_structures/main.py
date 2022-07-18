# List, Tuple, Set, Dictionary, Queue, and Stack

# List

# homogeneous vs heterogeneous
# homogeneous is a list of the same data type
# heterogeneous is a mixture list of different data types (int, float, bool, strings, etc... )

# letters = ["a", 'b', "c", 'd', 'e']
# letters[0] = "A"
# numbers = list(range(20))
# print(numbers[::2])
# print(numbers[::-1])
# print(letters[-2])
# print(letters[0:3])
# print(letters[:3])
# print(letters[0:])
# print(letters[:])
# print(letters)
# print(letters[:-2])
# print(letters[::2])  # 2 is the step
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)
# zeros = [0] * 5
# print(zeros)
# combined = zeros + letters
# print(combined)
# numbers = list(range(20))
# chars = list("Hello World")
# print(numbers, chars)
# print(len(chars))

# List unpacking
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# first, second, third, *other = numbers
# first, *other, last = numbers

# print(f"First: {first}\nSecond: {second}\nThird: {third}\nOther Items: {other}")
# print(f"First: {first}\nIn between: {other}\nOther Items: {last}")

# looping over a list
# letters = ["a", 'b', "c", 'd', 'd', 'd']

# letters.append('e')

# if "e" in letters:
#     print(letters.index("e"))
# else:
#     print("Not found")

# print(letters.count("d"))

# # Add
# letters.insert(0, "-")
# letters.append('e')

# # Remove
# letters.remove("-")
# letters.pop()
# del letters[0: 2]
# letters.clear()
# print(letters)

# for letter in letters:
#     print(letter)

# for index, letter in enumerate(letters):
#     print(index, letter)
# This will return a readonly list of tuples. Each item side by side with its index


# numbers = [3, 51, 4, 8, 17, 93, 2, 62]
# numbers.sort()  # Ascending
# print(numbers)
# numbers.sort(reverse=True)  # Descending
# print(numbers)

# new_list = sorted(numbers, reverse= False)
# print(new_list)

# items = [
#     ("product1", 10),
#     ("product2", 12),
#     ("product3", 9),
# ]

# # Lambda Expression
# # lambda parameters: expression
# items.sort(key=lambda item: item[1])
# print(items)

# print("\nUsing Lambda expression functions: map() and filter() ")
# # Map
# prices = list(map(lambda item: item[1], items))
# print(prices)

# # Filter
# filtered_list = list(filter(lambda item: item[1] >= 10, items))
# print(filtered_list)

# # List Comprehension
# # [expression for item in items]
# print("\nUsing Comprehension")
# prices = [item[1] for item in items]
# print(prices)

# filtered_list = [item for item in items if item[1] >= 10]
# print(filtered_list)

# # Zip Function
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# # Convert this into a tuple
# combined_lists = list(zip("abc", list1, list2))
# print(combined_lists)

# Stack LIFO (Last In First Out) push and pop
# from collections import deque


# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print(stack)
# last = stack.pop()
# print(last)
# print(stack)
# print("Redirect", stack[-1])
# # stack.clear()
# if not stack:
#     print("Empty Stack")

# if stack:
#     print("Not Empty Stack")

# # Falsy Value: 0 [] "" None

# # Queue FIFO (First In First Out) enqueue and dequeue
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# first = queue.popleft()
# print(first)
# print(queue)
# # queue.clear()
# if not queue:
#     print("Empty")

# if queue:
#     print("Not Empty")

# Tuples
# A tuple is a readonly list, we can read but we can write, change, delete anything once it has created.

# point = 1, 2
# print(point)
# print(type(point))

# x, y = point
# print(f"X: {x}\tY: {y}")

# # Empty tuple
# point1 = ()
# print(point1)

# point2 = (1, 2) + (3, 4)
# print(point2)

# point2 = (1, 2) * 3
# print(point2)

# point3 = tuple("Hello World")
# print(point3)
# x = 10
# y = 11

# print(f"Before:\nx: {x}\ty: {y}")
# x, y = y, x
# print(f"After:\nx: {x}\ty: {y}")

# Arrays
# from array import array

# numbers = array("i", [1, 2, 3, 4, 5])
# numbers.append(6)
# numbers.pop()
# numbers.insert(7, 7)
# numbers[0] = 8.2
# print(numbers)

# Set
# A collection with no duplicates
# Set doesn't support indexing, so the items inside the set are unordered
# numbers = [1, 2, 2, 3, 4, 5, 6, 4]
# first = set(numbers)
# second = {1, 9}
# print(first | second)  # Union
# print(first & second)  # Intersection
# print(first - second)  # Difference
# print(first ^ second)  # Symmetric Difference

# second_set.add(9)
# second_set.pop()
# if 3 in second_set:
#     second_set.remove(3)
# second_set.clear()

# Dictionaries
# AKA Map or HashMap  in other programming languages
# It is a collection of key-value pairs

# dictionary = {
#     "id": 1,
#     "name": "Motasem Abu Nema",
#     "age": 22,
#     "university": "IUG",
#     "college": "IT",
#     "gpa": 85.0,
#     "graduated": False,
#     "hobbies": ["Reading", "Writing", "Playing chess"],
#     "address": {
#         "city": "Gaza",
#         "street": "Yaffa St.",
#     },
#     "contacts": {
#         "email": "moatasem.abunema@gmail.com",
#         "phone": "00970599838964",
#     }
# }

# # dictionary.popitem()  # to remove the last item in the dict

# # print(len(dictionary))
# # print(dictionary)
# # print(dictionary.items())
# # print(dictionary.keys())
# # print(dictionary.values())

# point = {"x": 1, "y": 2}
# print(point)

# # Iterables
# list()
# tuple()
# set()
# dict()

# # Primitives
# int()
# str()
# float()
# bool()

# point2 = dict(x=7, y=8, z=9)
# print(point2)

# print(point2["z"])

# del point2["x"]
# print(point2)
# if "w" in point2:
#     print("Found")

# print(point2.get('w'))


# # looping over a dictionary
# for student in dictionary.items():
#     print(student)

# for key, value in dictionary.items():
#     print(key, ":", value)

# list_comprehension = [i * 2 for i in range(5)]
# tuple_comprehension = tuple((i * 2 for i in range(5)))
# set_comprehension = {i * 2 for i in range(5)}
# dict_comprehension = {i: i * 2 for i in range(5)}

# print("List Comprehension", list_comprehension)
# print("Tuple Comprehension", tuple_comprehension)
# print("Set Comprehension", set_comprehension)
# print("Dictionary Comprehension", dict_comprehension)


# Generator Expressions
# Use Generators with high values, or infinite number of streams
# () Generators
# [] Lists {} Sets {} dictionaries tuple() tuples
# from sys import getsizeof

# values = (i * 2 for i in range(100000000000))
# print(values)
# print(getsizeof(values))


# values2 = [i * 2 for i in range(1000000)]
# print(getsizeof(values2))


# Unpacking or Spread Operator
# * unpacking operator for lists, and tuples, ** for dictionaries
# you can unpack any iterables (lists, tuples, sets, ranges, dictionaries, strings, etc...)
# numbers = [1, 2, 3, 4, 5]
# print(*numbers)

# values = range(5)
# print(*values)
# print(*"Hello World!")

# first = [1, 2, 3]
# second = [4, 5]
# print(*first, *second)


# point = {"x": 7, "y": 8, "z": 9}
# newdict = {**point, "z": 10}
# print(newdict)


# Exercise
def get_most_repetitive_char(string):
    char_frequency = {}
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    char_frequency_sorted = sorted(
        char_frequency.items(),
        key=lambda kv: kv[1],
        reverse=True)
    return char_frequency_sorted[0]


sentence = "This is a common interview question"

print(get_most_repetitive_char(sentence))
