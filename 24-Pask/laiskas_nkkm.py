import ssl

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://nkkm.lt/registracija/"
DRIVER_PATH = r"C:/"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)

# Vardo entry input :
query_field_vardas = driver.find_element(By.NAME, "Vardas")
query_field_vardas.send_keys("Nojus")
query_field_vardas.send_keys(Keys.ENTER)

# Pavardes entry input :
query_field_pavarde = driver.find_element(By.NAME, "Pavarde")
query_field_pavarde.send_keys("Rascius")
query_field_pavarde.send_keys(Keys.ENTER)

# Amziaus entry input :
query_field_amzius = driver.find_element(By.NAME, "Amzius")
query_field_amzius.send_keys("18")
query_field_amzius.send_keys(Keys.ENTER)

# Telefono entry input :
query_field_tel = driver.find_element(By.NAME, "Telefonas")
query_field_tel.send_keys("+37061246699")
query_field_tel.send_keys(Keys.ENTER)

# Gmail'o entry input :
query_field_gmail = driver.find_element(By.NAME, "El-pastas")
query_field_gmail.send_keys("rascius.nojus@gmail.com")
query_field_gmail.send_keys(Keys.ENTER)

# Filialo checkbox check :
driver.find_element(By.XPATH, '//*[@id="wpcf7-f1232-p392-o1"]/form/div[2]/div/span/span/span[2]/input').click()

# Checkboc check :
driver.find_element(By.CSS_SELECTOR, "wpcf7-form-control wpcf7-submit").click()

driver.close()
