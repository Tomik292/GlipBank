from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("../new_hodoor/Hodoor/node_modules/chromedriver/lib/chromedriver/chromedriver")
driver.get('https://glip.com/')

driver.find_element_by_id('sign_in').click()
time.sleep(1)
email = driver.find_element_by_name('email')
password = driver.find_element_by_name('password')

password.send_keys("MoT159357")
email.send_keys("tomas.houfek@eledus.cz")
driver.find_element_by_class_name("submit").click()
time.sleep(20)

all_groups = driver.find_elements_by_class_name("grouptab")
group_ids, group_names, visible_groups = [], [], []

for group in all_groups:
    print(group.get_attribute("style"),group.get_attribute("id"))
    if (group.get_attribute("style") == 'display: block;'):
        visible_groups.append(group.get_attribute("id"))


for grp_id in visible_groups:
    driver.find_element_by_id(grp_id).click()
    print(grp_id)
    time.sleep(1)
    try:
        driver.find_element_by_class_name("post_text").click()
    except:
        pass
    driver.execute_script("window.scrollTo(0, -250)")
    texts = driver.find_elements_by_class_name("post_text")
    for text in texts:
        text_value = text.get_attribute('innerHTML')
        print(text_value)
    time.sleep(2)
