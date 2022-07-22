from multiprocessing.connection import wait
from xml.dom.minidom import Element
from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



driver = webdriver.Chrome()
time.sleep(5)
# assign your website
web = 'https://www.amazon.de'
driver.get(web)
driver.maximize_window
#coockies click
jazuCookies= search_button = driver.find_element(By.ID, 'sp-cc-accept').click()
# assign any keyword for searching
Einkaufsliste = ["Adidas Herren Questar Flow Laufschuhe", "Puma Tazon 6"," Air Max Nike Herren"]

#Einkaufsliste durchgehen:
for x in range(len(Einkaufsliste)):
    keyword = Einkaufsliste[x]
    print (x)
    print(keyword)
    driver.implicitly_wait(2)
# create WebElement for a search box
    search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
    driver.maximize_window()
# type the keyword in searchbox
    search_box.send_keys("")
    search_box.send_keys(keyword)
# create WebElement for a search button
    search_button = driver.find_element(By.ID, 'nav-search-submit-button').click()
# wait for the page to download
    driver.implicitly_wait(5)
#select first result

    auswahl=driver.find_element(By.XPATH,"//div[contains(@data-cel-widget,'search_result_2')]").click()
    driver.implicitly_wait(5)

#PulldownMenü für Größe
    driver.implicitly_wait(5)

    driver.implicitly_wait(5)

    schuhsize=  driver.find_element(By.ID, "native_dropdown_selected_size_name")
    driver.implicitly_wait(4)
    size = Select(driver.find_element(By.ID, "native_dropdown_selected_size_name"))
    size.select_by_index(4)

    sleep(5)

#in den Einkaufskorb
    driver.implicitly_wait(5)
    warenkorb=driver.find_element(By.ID,'add-to-cart-button')
    driver.implicitly_wait(5)
    warenkorb.click()
aufrufen=driver.find_element(By.ID,'nav-cart').click()

