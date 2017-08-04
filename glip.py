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
'''driver.find_element_by_id("49818214402").click()
time.sleep(10)
groups = driver.find_elements_by_class_name("grouptab")
group_ids, group_names = [], []
texts = driver.find_elements_by_class_name("post_text")
'''

all_groups = driver.find_elements_by_class_name("grouptab")
group_ids, group_names, visible_groups = [], [], []

for group in all_groups:
    print(group.get_attribute("style"))
    if group.get_attribute("style") == "display: block;":
        visible_groups.append(group.get_attribute("id"))

visible_groups.pop(0)
print(group_ids)
for grp_id in group_ids:
    driver.find_element_by_id(grp_id).click()
    print(grp_id)
    time.sleep(2)
'''        
for text in texts:
    text_value = text.get_attribute('innerHTML')
    print(text_value)

print(group_ids,group_names)

for group in groups:
    group_ids.append(group.get_attribute("id"))
'''
