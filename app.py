# from pathlib import Path
# from zipfile import ZipFile

# r -> Read, w -> Write, x -> exclusive create, a -> append
# with ZipFile("files.zip", "w") as zip:
#     for path in Path("08_modules/ecommerce").rglob("*.*"):
#         zip.write(path)

# with ZipFile("files.zip", "r") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("08_modules/ecommerce/shopping/sales.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")

# from time import ctime
# import shutil
# path = Path("08_modules/ecommerce/__init__.py")
# target = Path() / "__init__.py"

# shutil.copy(path, target)
# paths = [p for p in path.iterdir() if p.is_dir()]
# py_files = [p for p in path.rglob("*.py")]
# print(paths)
# print(py_files)

# path.exists()
# path.rename("init.py")
# path.unlink()
# print(ctime(path.stat().st_ctime))
# print(path.read_bytes())
# print(path.read_text())
# print(path.read_text())

# path.write_text("...")
# path.write_bytes()


# import csv

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 7])
#     writer.writerow([1002, 3, 12])

# with open("data.csv") as file:
#     reader = csv.reader(file)
#     # print(list(reader))
#     for row in reader:
#         print(row)

# import sqlite3
# import json
# from pathlib import Path

# # movies = json.loads(Path('09_python_standard_library/movies.json').read_text())
# # print(movies)


# create_command = """
#                 CREATE TABLE Movies(
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     title TEXT NOT NULL,
#                     year TEXT
#                 );
# """

# insert_command = "INSERT INTO Movies VALUES(?, ?, ?)"

# delete_command = "DELETE FROM Movies WHERE id =?"

# update_command = "UPDATE Movies SET ?"

# select_command = "SELECT * FROM Movies"


# with sqlite3.connect("db.sqlite3") as connection:
#     # connection.execute(create_command)
#     # for movie in movies:
#     #     connection.execute(insert_command, tuple(movie.values()))
#     # connection.commit()
#     cursor = connection.execute(select_command)
#     # for row in cursor:
#     #     print(row)
#     movies_list = cursor.fetchall()
#     print(movies_list)

# 7 Things I Never Knew About Python Until Recently

# 1) Private Variables In Classes Are Not Really Private
# 2) We Can Use type() To Create Classes Without The ‘class’ Keyword
# 3) We Get This If We Add A List To Itself
# 4) Infinity Values In Python
# 5) We Can Use Classes As Decorators
# 6) We Can Use Chinese Characters As Variable Names
# 7) We Can Use eval() To Run Python Code In Strings
