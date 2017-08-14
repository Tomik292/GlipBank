from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

def waitForElementID(drive,elementID):
    element = WebDriverWait(drive, 30).until(
        EC.presence_of_element_located((By.ID, elementID))
    )
    return element

def waitForElementClassName(drive,elementClass):
    element = WebDriverWait(drive, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, elementClass))
    )
    return element
    
def waitForElementClassNameShort(drive,elementClass):
    element = WebDriverWait(drive, 1).until(
    EC.presence_of_element_located((By.CLASS_NAME, elementClass))
    )
    return element   
    
def waitForElementName(drive,elementName):
    element = WebDriverWait(drive, 30).until(
        EC.presence_of_element_located((By.NAME, elementName))
    )
    return element

def waitForElementTagName(drive,elementTagName):
    element = WebDriverWait(drive, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, elementTagName))
    )
    return element    

driver = webdriver.Chrome("../new_hodoor/Hodoor/node_modules/chromedriver/lib/chromedriver/chromedriver")
driver.get('https://glip.com/')
    
waitForElementID(driver,"sign_in").click()
email = waitForElementName(driver,"email")
password = waitForElementName(driver,"password")


password.send_keys("MoT159357")
email.send_keys("tomas.houfek@eledus.cz")
waitForElementClassName(driver,"submit").click()

waitForElementClassName(driver,"grouptab")
all_groups = driver.find_elements_by_class_name("grouptab")
group_ids, group_names, visible_groups = [], [], []

for group in all_groups:
    if (group.get_attribute("style") == 'display: block;'):
        visible_groups.append({
            "id" : group.get_attribute("id"),
            "name" : group.text,
            })

for grp_id in visible_groups:
    waitForElementID(driver,grp_id["id"]).click()
    print(grp_id["name"])
    find_elem = None
    while not find_elem:
        try:
            find_elem = waitForElementClassNameShort(driver,"calls-to-action-welcome")
        except:
            waitForElementTagName(driver,"author").click()
            driver.execute_script("window.scrollTo(0, -200)")
        print(find_elem, grp_id["name"])
    texts = driver.find_elements_by_class_name("post_text")
    for text in texts:
        text_value = text.get_attribute('innerHTML')
        print(text_value)
    time.sleep(2)
