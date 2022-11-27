# Types & Type hints

""" Tradeoffs when you are dealing with types & type hints:
    1. Complex types may lead to cryptic error messages.
    2. Types may restrict functionality.
    3. Types are not yet that common in Python packages.
"""


class Book:
    def __init__(self, author: str, title: str, pages: int) -> None:
        self.author = author
        self.title = title
        self.pages = pages

    def __len__(self) -> int:
        return self.pages


def main():
    my_str = "hello"
    print(len(my_str))
    my_list = [23, 53, 92, 12]
    print(len(my_list))
    my_dict = {'one': 123, 'two': 456, 'three': 789}
    print(len(my_dict))
    my_book = Book(author="Robert C. Martin", title="Clean Code", pages=464)
    print(len(my_book))


if __name__ == '__main__':
    main()
