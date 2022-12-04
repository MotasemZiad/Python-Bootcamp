""" The ultimate guide to write a good function in python:
    1. Do one thing, and do it well.
    2. Separate commands from queries.
    3. Only request information you actually need.
    4. Keep the number of parameters minimal.
    5. Don't create and use an object in the same place.
    6. Don't use flag arguments.
    7. Remember that functions are object.
    Bonus: Follow the naming convention and the style guide of your language.
    a. If a function has and like create_user_and_store _in_db check if it does one thing.
    b. Always try to shorten the name of the function (ex: publish_info_to_library(lib) should be publish_info_to(library))
    c. Function names should be Actions (Verbs), but arguments should be Nouns (ex: greeting(say_hi_to: str) should be greet(name: str))
    d. Make sure you use the same vocabulary everywhere (ex: get() or fetch(), post() or store())
    e. Use the full name instead of the first character (n -> number, l -> library, n -> name)   
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

import logging


class PaymentHandler(Protocol):
    def handle_payment(self, amount: int) -> None:
        ...


class StripePaymentHandler:
    def handle_payment(self, amount: int) -> None:
        logging.info(f"Charging ${amount/100:.2f} using Stripe")


class PayPalPaymentHandler:
    def handle_payment(self, amount: int) -> None:
        logging.info(f"Charging ${amount/100:.2f} using PayPal")


PRICES = {
    "burger": 15_00,
    "fries": 5_00,
    "drink": 2_00,
    "salad": 3_00,
}


def order_food(items: list[str], payment_handler: PaymentHandler) -> None:
    total = sum(PRICES[item] for item in items)
    logging.info(f"Order total is ${total/100:.2f}.")
    payment_handler.handle_payment(total)
    logging.info("Order completed.")


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
    # card = Card(
    #     number="8976325968451298",
    #     exp_month=1,
    #     exp_year=2025,
    # )
    # ahmed = Customer(
    #     name="Ahmed Ali",
    #     phone="+00970598926087",
    #     card=card
    # )

    # ahmed.cc_valid = validate_card(card)
    # print(f"Is Ahmed's card valid? {ahmed.cc_valid}")
    # print(ahmed)
    payment_handler = StripePaymentHandler()
    logging.basicConfig(level=logging.INFO)
    order_food(["burger", "fries", "drink"], payment_handler)


if __name__ == "__main__":
    main()
