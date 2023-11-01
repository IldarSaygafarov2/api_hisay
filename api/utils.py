import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


def get_address_by_loc(location):
    url = "https://www.google.com/maps/place/"
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Edge(options=options)
    driver.get(url)
    elem = driver.find_element(By.ID, 'searchboxinput')
    elem.clear()
    elem.send_keys(location)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    text = driver.find_element(By.CLASS_NAME, 'DkEaL').text
    return text
