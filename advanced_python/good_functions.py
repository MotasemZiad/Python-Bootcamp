""" The ultimate guide to write a good function in python:
    1. Do one thing, and do it well.
    2. Separate commands from queries.
    3. Only request information you actually need.
    4. Keep the number of parameters minimal.
    5. Don't create and use an object in the same place.
    6. Don't use flag arguments.
    7. Remember that functions are object.
    Bonus: Follow the naming convention and the style guide of your language. 
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Customer:
    name: str
    phone: str
    cc_number: str
    cc_exp_month: int
    cc_exp_year: int
    cc_valid: bool = False


def luhn_checksum(card_number: str) -> bool:
    def digits_of(number: str) -> list[int]:
        return [int(d) for d in number]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(str(digit * 2)))
    return checksum % 10 == 0


def validate_card(customer: Customer) -> bool:
    customer.cc_valid = (
        luhn_checksum(customer.cc_number) and datetime(
            customer.cc_exp_year, customer.cc_exp_month, 1) > datetime.now()
    )

    return customer.cc_valid


def main() -> None:
    ahmed = Customer(
        name="Ahmed Ali",
        phone="+00970598926087",
        cc_number="1222093487125099",
        cc_exp_month=1,
        cc_exp_year=2025,
    )
    is_valid = validate_card(ahmed)
    print(f"Is Ahmed's card valid? {is_valid}")
    print(ahmed)


if __name__ == "__main__":
    main()
