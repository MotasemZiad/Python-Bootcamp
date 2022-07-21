# Python Standard Library
# Work with Files, SQLite, Data/Time, Random Values, Email

# python_exercises = "Practice Python"
# pythonista = "When you committed to the naming convention and best practices"

# print(pythonista)
# print(python_exercises)

# Working with Paths
# from pathlib import Path

# Path(r"C:\Program Files\Microsoft")  # Windows
# Path("/usr/local/bin")  # Linux
# Path()
# my_path = Path() / "ecommerce" / "__init__.py"
# Path.home()

# path = Path("../08_modules/ecommerce/__init__.py")
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_stem("file")
# path = path.with_suffix(".txt")
# print(path.absolute())
# print(path.exists())
# print(path.is_file())
# print(path.is_dir())
# print(path.is_absolute())

# Working with Directories
# path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# Posix Paths for unix-like operating systems (Mac, Linux)
# Windows Paths for Microsoft windows


# paths = [p for p in path.iterdir()]
# print(paths)

# Working With Files

# Working with Zip Files

# Working with CSV Files
# CSV -> Comma-Separated Values: is a text file that has a specific format which allows data to be saved in a table structured format.

# Working with Json
# Json Serialization: aka. (Json Encoding) It is the process of converting an object into a json format.
# Json Deserialization: aka. (Json Decoding) It is the process of converting a json into an object format.
# json.pumbs() Json Encoding
# # json.loads() Json Decoding
# import json
# from pathlib import Path

# movies = [
#     {
#         "id": 1,
#         "title": "The Terminator",
#         "year": 1984
#     },
#     {
#         "id": 2,
#         "title": "The Garden",
#         "year": 1990
#     },
# ]

# Converting Python objects to Json

# data = json.dumps(movies)
# # print(data)
# Path("movies.json").write_text(data)

# Converting Json to Python objects
# data = Path("movies.json").read_text()
# movies = json.loads(data)
# print(movies)
# print(movies[0])


# Working with Local Databases (SQLite database)

# Working with Timestamp
# Work with Date & Time
# Timestamp VS. DateTime
# import time
# time module for timestamp, datetime module for Datetime
# print(time.ctime(time.time()))


# def send_emails():
#     for i in range(10000):
#         pass


# start = time.time()
# send_emails()
# end = time.time()
# duration = end - start
# print(duration)

# from datetime import datetime
# import time

# print(datetime(year=2018, month=5, day=7, hour=9, minute=35, second=39))
# print(datetime.now())
# dt = datetime.now()
# dt2 = datetime(2019, 9, 9)
# ts = datetime.ctime(dt)

# print("DateTime", dt)
# print("TimeStamp", ts)

# converted_from_string_datetime = datetime.strptime("17/05/2015", "%d/%m/%Y")
# print(converted_from_string_datetime)

# dt = datetime.fromtimestamp(time.time())
# print(dt)

# print(f"{dt.year}/{dt.month}/{dt.day}")

# # strptime VS. strftime
# datetime.strptime("17/05/2015", "%d/%m/%Y")
# str_datetime = dt.strftime("%y/%m")
# print(str_datetime)
# print(dt > dt2)
# print("DT 1", dt)
# print("DT 2", dt2)


# Working with Time Delta which represent a duration

# from datetime import datetime, timedelta

# dt1 = datetime(2018, 7, 8) + timedelta(days=1)
# print(dt1)
# dt2 = datetime.now()
# duration = dt2 - dt1
# print(duration)
# print(type(duration))

# print("Seconds", duration.seconds)
# print("Days", duration.days)
# print("Total Seconds", duration.total_seconds())


# Generating Random Values
# import random
# import math
# import string
# print(math.trunc(random.random() * 100))
# print(random.randint(1, 100))
# print(random.choice([1, 2, 3, 4, 5]))
# print(random.choices([1, 2, 3, 4, 5], k=2))
# # print("Generated Random Password:", "".join(random.choices(
# #     "abcdefghijklmnopqrstuvwxyz!@#$%&*_?^()0123456789", k=8)))
# print("Generated Random Password:", "".join(random.choices(
#     string.ascii_letters + string.digits + string.punctuation, k=8)))

# numbers = list(range(0, 10))
# random.shuffle(numbers)
# print(numbers)

# Converting a list into a string using join method: "".join(list)
# print(string.ascii_letters)
# print(string.punctuation)
# print(string.digits)


# Opening the browser
# import webbrowser

# print("Deployment Completed Successfully")
# webbrowser.open("https://www.linkedin.com/in/motasemabunema")
# webbrowser.open_new("https://www.github.com/motasemziad")
# webbrowser.open_new_tab("http://motasemziad.github.io/Personal-Website/")

# Sending Emails:
# MIME: Multipurpose Internet Mail Extension
# It is an extension of the original Simple Mail Transport Protocol (SMTP) email protocol.
# It lets users exchange different kinds of data files,
# including audio, video, images and application programs, over email.
# TLS: Transport Layer Security
# with this protocol all the message that have sent over the internet where encrypted

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from importlib.resources import read_text
# from pathlib import Path
# from re import template
# from string import Template
# import smtplib

# template = Template(Path("template.html").read_text())

# message = MIMEMultipart()
# message['from'] = "Motasem Abu Nema"
# message['to'] = "mnima2000@students.iugaza.edu.ps"
# message['subject'] = "This is a test email"

# body = template.substitute({
#     "name": "John Doe",
# })
# # body = template.substitute(name="Jane Doe")

# message.attach(MIMEText(body, "html"))
# message.attach(MIMEImage(Path("github-logo.png").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login(user="mnima2000@students.iugaza.edu.ps", password="**********")
#     smtp.send_message(message)
#     print("Sent...")


# Command-line arguments

# import sys

# if len(sys.argv) == 1:
#     print("USAGE: python3 main.py <password>")
# else:
#     password = sys.argv[1]
#     print("Password", password)

# Running External Programs

# import subprocess

# completed = subprocess.run(
#     ["ls", "-l"], capture_output=True, check=True, text=True)
# print("args: ", completed.args)
# print("returncode: ", completed.returncode)
# print("stdout: ", completed.stdout)
# print("stderr: ", completed.stderr)


# completed = subprocess.run(
#     ["py", "./other.py"],
#     capture_output=True,
#     text=True)
# print("args: ", completed.args)
# print("returncode: ", completed.returncode)
# print("stdout: ", completed.stdout)
# print("stderr: ", completed.stderr)
