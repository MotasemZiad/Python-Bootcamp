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
from typing import Protocol


@dataclass
class Card:
    number: str
    exp_month: int
    exp_year: int


@dataclass
class Customer:
    name: str
    phone: str
    card: Card
    cc_valid: bool = False


class CardInfo(Protocol):
    @property
    def number(self) -> str:
        ...

    @property
    def exp_month(self) -> int:
        ...

    @property
    def exp_year(self) -> int:
        ...


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


def validate_card(card: CardInfo) -> bool:
    return (
        luhn_checksum(card.number)
        and datetime(card.exp_year, card.exp_month, 1) > datetime.now()
    )


def main() -> None:
    card = Card(
        number="8976325968451298",
        exp_month=1,
        exp_year=2025,
    )
    ahmed = Customer(
        name="Ahmed Ali",
        phone="+00970598926087",
        card=card
    )

    ahmed.cc_valid = validate_card(card)
    print(f"Is Ahmed's card valid? {ahmed.cc_valid}")
    print(ahmed)


if __name__ == "__main__":
    main()
