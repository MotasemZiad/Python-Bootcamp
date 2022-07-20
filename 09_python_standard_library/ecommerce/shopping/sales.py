# Absolute Path VS. Relative Path
# Absolute Path is the recommended approach
# from ecommerce.customer.contact import contact_customer
# from ..customer.contact import contact_customer
# contact_customer()

print("Sales Initialized", __name__)


def calc_tax():
    pass


def calc_shipping():
    pass


if __name__ == "__main__":
    print("Sales started")
    calc_tax()
