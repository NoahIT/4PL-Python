from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://www.python.org"
DRIVER_PATH = r"C:/"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)

query_field = driver.find_element(By.NAME, "q")
query_field.send_keys("for")
query_field.send_keys(Keys.ENTER)

titles = driver.find_elements(By.TAG_NAME, "h3")

for title in titles:
    print(title.text)

# EVENTAI :
# menu = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div/div/ul')
#
# events = menu.find_elements(By.CSS_SELECTOR, "li a")
#
# print(menu)
# for event in events:
#     print(events.text)
#
# driver.quit()
