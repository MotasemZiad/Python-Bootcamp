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