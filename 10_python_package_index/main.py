# Python Package Index (PPI)
# Some pip useful commands to use
# ! Semantic version: 2.28.1 => major.minor.bug_fixes
# ? pip install package_name
# ? pip install --upgrade pip # the latest version of pip
# ? pip install --upgrade package_name # To upgrade the package to the latest version
# ? pip install package_name==2.9.0
# ? pip install package_name==2.9.*
# ? pip uninstall package_name
# ? pip download package_name
# ? pip search package_name

import requests

get_users = requests.get(url="https://jsonplaceholder.typicode.com/users")
print(get_users.status_code)
print(get_users.headers['Content-Type'])
print(get_users.encoding)
print(get_users.text)
print(get_users.json())


# Virtual Environment -> Docker, kubernetes, etc...
# Create an isolated virtual environment and install the dependencies you want.

# Uploading a package to pypi.org
# Docstring
# Pydoc
