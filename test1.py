from multiprocessing.connection import wait
from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
time.sleep(5) # Let the user actually see something!
# assign your website to scrape
web = 'https://www.amazon.de'
driver.get(web)
driver.maximize_window
#coockies click
jazuCookies= search_button = driver.find_element(By.ID, 'sp-cc-accept').click()
# assign any keyword for searching

keyword = "Adidas Schuhe"
driver.implicitly_wait(2)
# create WebElement for a search box
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
driver.maximize_window()
# type the keyword in searchbox
search_box.send_keys(keyword)
# create WebElement for a search button
search_button = driver.find_element(By.ID, 'nav-search-submit-button').click()
# wait for the page to download
driver.implicitly_wait(5)
#select first result
##INFO: Im Laufe des Tages gab es neue "Erste Treffer" in der Suche die keinerlei Größenauswahl benötigten, daher habe ich den Klick auf das erst Element gelegt welches eine Schuhgröße zur Auwahl stellt  [3] bevor der Srtikel in den Warenkorb gelegt werden kann.
auswahl=driver.find_element(By.XPATH,"//div[contains(@data-cel-widget,'search_result_3')]").click()
driver.implicitly_wait(10)
#PulldownMenü für Größe
driver.implicitly_wait(5)

driver.implicitly_wait(5)


schuhsize=  driver.find_element(By.ID, "native_dropdown_selected_size_name")
driver.implicitly_wait(5)
size = Select(driver.find_element(By.ID, "native_dropdown_selected_size_name"))
size.select_by_index(2)

sleep(5)

#in den Einkaufskorb
driver.implicitly_wait(5)
warenkorb=driver.find_element(By.ID,'add-to-cart-button')
driver.implicitly_wait(5)
warenkorb.click()

#ddto=  driver.find_element(By.CLASS_NAME, "a.button-input").click()
#driver.implicitly_wait(25)
