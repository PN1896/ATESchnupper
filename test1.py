from select import select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
time.sleep(5) # Let the user actually see something!
# assign your website to scrape
web = 'https://www.amazon.de'
driver.get(web)



# assign any keyword for searching
keyword = "Adidas Schuhe"
# create WebElement for a search box
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
# type the keyword in searchbox
search_box.send_keys(keyword)
# create WebElement for a search button
search_button = driver.find_element(By.ID, 'nav-search-submit-button').click()
# wait for the page to download
driver.implicitly_wait(5)
#select first result
ergebnise=  driver.find_element(By.CLASS_NAME, "s-image").click()
driver.implicitly_wait(10)
driver.implicitly_wait(5)
schuhsize=  driver.find_element(By.ID, "native_dropdown_selected_size_name")
#schuhsize=  driver.find_element(By.CLASS_NAME, "a-native-dropdown a-declarative")
driver.implicitly_wait(5)
schuhsize=Select.select_by_index(0,2)
driver.implicitly_wait(5)


inKorb = driver.find_element(By.ID, 'dd-to-card-button').click()
addto=  driver.find_element(By.CLASS_NAME, "a-button-inner").click()
# quit the driver after finishing scraping (please keep this line at the bottom)

driver.quit()

