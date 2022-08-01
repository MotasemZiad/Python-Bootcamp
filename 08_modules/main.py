# Module:
# a module is a file that contains some lines of code.
# from sales import * # bad practice
# import sales
# from ecommerce import sales
# from ecommerce.shopping import sales
# import sys
# print(sys.path)
# Package: a directory
# Module: a file

# sales.calc_shipping()
# sales.calc_tax()

# # The dir function is used for debugging
# print(dir(sales))
# print(sales.__name__)
# print(sales.__package__)
# print(sales.__file__)

# from pathlib import Path

# path = Path("../08_modules/ecommerce")

# for p in path.iterdir():
#     print(p)
