import ssl

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL_1 = "https://www.skytech.lt/"
URL_2 = "https://www.topocentras.lt/"
URL_3 = "https://www.varle.lt/"

DRIVER_PATH = r"C:\Users\Admin\Desktop\d\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

def search_skytech(): #SKYTECH.LT

    driver.get(URL_1)

    query_field_search = driver.find_element(By.CSS_SELECTOR, '#body > div.pageouter > div.pagewrapper > div.pageheader > table > tbody > tr > td:nth-child(2) > div > form > div.search-wrap > input.search-field.inactive')
    query_field_search.send_keys("Logitech M185 Wireless Mouse Blue")
    query_field_search.send_keys(Keys.ENTER)

    price = driver.find_element(By.XPATH, '//*[@id="centerpanel"]/div[1]/table[1]/tbody/tr[2]/td[5]/strong/strong')
    price = price.text

    print("Price in Skytech.lt " + price + " \n")

# def search_varle(): #VARLE.LT
#
#     driver.get(URL_2)
#
#     query_field_search = driver.find_element(By.CSS_SELECTOR, 'body > div.HEADER.sticky > div.header-bar > form > form > div > div > div > input')
#     query_field_search.send_keys("Logitech M185 Wireless Mouse Blue")
#     query_field_search.send_keys(Keys.ENTER)
#
#     item = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]")
#     item.click()
#
#     price = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div[3]/div/div/span')
#     price = price.text
#
#     print("Price in Varle.lt " + price + " \n")
#
# def search_topocentras(): #TOPOCENTRAS.LT
#
#     driver.get(URL_3)
#
#     query_field_search = driver.find_element(By.XPATH, '//*[@id="root"]/header[1]/div[1]/div[2]/div[1]/div[1]/input')
#     query_field_search.send_keys("Logitech M185 Wireless Mouse Blue")
#     query_field_search.send_keys(Keys.ENTER)
#
#     search_button = driver.find_element(By.CLASS_NAME, "HeaderContent-searchButton-1mR")
#     search_button.click()
#
#     item = driver.find_element(By.XPATH, '//*[@id="categoryPage"]/article/div[1]/a')
#     item.click()
#
#     price = driver.find_element(By.XPATH, '//*[@id="productPage"]/div[2]/div/article/div[2]/div[2]/div[1]/div[1]/div[2]/div/span')
#     price = price.text
#
#     print("Price in Topocentras.lt " + price + " \n")


search_skytech()
# search_topocentras()
# search_skytech()