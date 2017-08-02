'''from lxml import html
import requests
page = requests.get('https://cs.wikipedia.org/wiki/USS_Gerald_R._Ford_(CVN-78)')
tree = html.fromstring(page.content)
authors = tree.xpath('//h1[@class="firstHeading"]/text()')
messeges = tree.xpath('//span[@class="mw-headline"]/text()')

print(authors,messeges)
'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("../new_hodoor/Hodoor/node_modules/chromedriver/lib/chromedriver/chromedriver")
driver.get('https://glip.com/')


#wait_for_element_to_be_clickable_with_css_selector_click(driver,"//li[@class='navItem signIn']")
driver.find_element_by_id('sign_in').click()
time.sleep(1)
email = driver.find_element_by_name('email')
password = driver.find_element_by_name('password')

password.send_keys("MoT159357")
email.send_keys("tomas.houfek@eledus.cz")
driver.find_element_by_class_name("submit").click()
time.sleep(20)
groups = driver.find_elements_by_class_name("grouptab")
texts = driver.find_elements_by_class_name("post")
for group in groups:
    group_name = group.get_attribute('innerHTML')
    print(group_name)
for text in texts:
    text_value = group.get_attribute('innerHTML')
    print(text_value)
