# Types and Type Hints in Python
# from typing import Callable

# def add_three(x: int) -> int:
#     return x + 3


# def multiply_by_two(x: float) -> float:
#     return x * 2.0


# def compute_stats(users, plans, products):
#     # Some complicated code here that does something
#     pass


# IntFunction = Callable[[int], int]

class Book:
    def __init__(self, author: str, title: str, pages: int):
        self.author = author
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages


def main():
    my_str="hello"
    print(len(my_str))
    my_list=[34, 45, 56, 67]
    print(len(my_list))
    my_dict={"one": 1, "two": 2, "three": 3}
    print(len(my_dict))
    my_book=Book("Robert Martin", "Clean Code", 464)
    print(len(my_book))
    
    # my_var: IntFunction = multiply_by_two
    # my_var = 5
    # my_var = True
    # my_var = 3.14
    # my_var = None
    # my_var = (5, 8)
    # my_var = [2, 3, 5]
    # my_var = {2, 3, 5, 7}
    # my_var = {'name': "Motasem Abu Nema", 'age': 22, 'graduated': False,
    #           'gpa': 85.82, 'skills': ['Python', 'API', 'AWS', 'Linux']}

    # print(my_var(5))
    # print(type(my_var))


if __name__ == "__main__":
    main()
