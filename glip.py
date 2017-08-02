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



driver = webdriver.Chrome("../new_hodoor/Hodoor/node_modules/chromedriver/lib/chromedriver/chromedriver")
driver.get('https://glip.com/')
driver.find_element_by_id("sign_in").click()
username = driver.find_element_by_name("email")
password = driver.find_element_by_name("password")

password.send_keys("MoT159357")
username.send_keys("tomas.houfek@eledus.cz")
driver.find_element_by_class_name("submit").click()
