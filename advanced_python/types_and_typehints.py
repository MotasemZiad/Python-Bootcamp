from typing import Callable

IntFunction = Callable[[int], int]


def multiply_by_two(x: float) -> float:
    return x * 2.0


def add_three(x: int) -> int:
    return x + 3


def compute_stats(users, plans, products):
    # some complicated code..
    pass


def main():
    my_var: IntFunction = multiply_by_two
    print(my_var(5))


if __name__ == '__main__':
    main()
