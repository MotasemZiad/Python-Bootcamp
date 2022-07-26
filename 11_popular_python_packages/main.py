# Working with popular python packages (requests, selenium, numpy, web scraping)

# API -> Application Programming Interface
# Working with Yelp API

# import requests
# import config

# location = "NYC"
# term = "Barber"

# # URL = f"https://api.yelp.com/v3/businesses/search?location={location}&term={term}"
# URL = "https://api.yelp.com/v3/businesses/search"

# HEADERS = {
#     "Authorization": f"Bearer {config.API_KEY}"
# }

# PARAMS = {
#     "location": location,
#     "term": term,
# }
# response = requests.get(URL, headers=HEADERS, params=PARAMS)
# businesses = response.json()['businesses']

# print(response.status_code)

# good_barbers = [business['name']
#                 for business in businesses if business['rating'] >= 4.5 if not business['is_closed']]

# print(good_barbers)

# Sending Text Messages with Twilio https://twilio.com
# from twilio.rest import Client
# import config
# client = Client(config.ACCOUNT_SID, config.AUTH_TOKEN)

# done = client.messages.create(
#     to="+970599838964",
#     from_="+13374545789",
#     body="Love you baby ❤",
# )

# if(done):
#     print("Sent")

# Browser Automation
# Selenium for browser automation
# Some PROBLEMS require a delay to be solved
# import config
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# browser = webdriver.Chrome()
# wait = WebDriverWait(browser, 20)
# browser.get("https://github.com")


# signin_link = browser.find_element(by=By.LINK_TEXT, value="Sign in")
# signin_link.click()

# wait.until(EC.visibility_of_element_located((By.ID, 'login_field')))

# username_box = browser.find_element(by=By.ID, value="login_field")
# username_box.send_keys(config.GITHUB_USERNAME)
# password_box = browser.find_element(by=By.ID, value="password")
# password_box.send_keys(config.GITHUB_PASSWORD)
# password_box.submit()

# assert config.GITHUB_USERNAME in browser.page_source

# browser.quit()

# Web Scaping
# Parsing the HTML behind a web page, get rid of all the html tags, and extract the actual data.
# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://stackoverflow.com/questions")
# soup = BeautifulSoup(response.text, "html.parser")

# questions = soup.select(
#     ".s-post-summary--content")
# # print(type(questions[0]))
# i = 0
# for question in questions:
#     print(f"{i+1}) ", question.select_one(".s-link").get_text())
#     i += 1

# # print("Description: ", questions[0].select_one(".s-post-summary--content-excerpt").get_text())
# # print(questions[0].get("class", 0))
# # print(soup.prettify().encode('cp1252', errors='ignore'))

# Working with PDFs
import PyPDF2

# rb => read in binary

# with open("./11_popular_python_packages/first.pdf", "rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotate_clockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.add_page(page)
#     with open("rotated.pdf", "wb") as output:
#         writer.write(output)


# with open("./11_popular_python_packages/third.pdf", "rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
#     page = reader.getPage(4)
#     page.rotate_clockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.add_blank_page(250, 250)
#     with open("blanked.pdf", "wb") as output:
#         writer.write(output)

merger = PyPDF2.PdfFileMerger()
file_names = ["./11_popular_python_packages/first.pdf",
              "./11_popular_python_packages/second.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write('combined.pdf')
