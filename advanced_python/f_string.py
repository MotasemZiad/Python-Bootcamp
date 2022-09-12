import datetime
from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str


def main():
    number = 900
    print(f"The number is {number:x}.")  # Hexadecimal representation
    print(f"The number is {number:o}.")  # Octal representation
    print(f"The number is {number:e}.")  # Scientific representation
    print(f"The number is {102.72348912:0.2f}.")  # Floating-point number
    # Floating-point with comma
    print(f"Elon Musk buy Twitter for ${44000000000:,.2f}")
    print(f"Percentage {0.23472:.2%}")


if __name__ == "__main__":
    main()
