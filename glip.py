from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import os.path
import getpass
import time

def waitForElement(drive,element_type,element,wait_time): #waiting for elements to be located function
    if element_type == "ID":
        element = WebDriverWait(drive, wait_time).until(
            EC.presence_of_element_located((By.ID, element))
        )
        return element
    elif element_type == "CLASS":
        element = WebDriverWait(drive, wait_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, element))
        )
        return element
    elif element_type == "NAME":
        element = WebDriverWait(drive, wait_time).until(
            EC.presence_of_element_located((By.NAME, element))
        )
        return element
    elif element_type == "TAG":
        element = WebDriverWait(drive, wait_time).until(
            EC.presence_of_element_located((By.TAG_NAME, element))
        )
        return element

if not os.path.exists("./../"+time.strftime("%d.%m.%Y")+" saves"):
    os.makedirs("./../"+time.strftime("%d.%m.%Y")+" saves")

your_mail = str(input("Your e-mail: "))   #your glip mail
your_password = getpass.getpass("Your password: ")   #your glip password

driver = webdriver.Chrome("./../node_modules/chromedriver/bin/chromedriver")
driver.get('https://glip.com/')

waitForElement(driver,"ID","sign_in",60).click()
email = waitForElement(driver,"NAME","email",60)
password = waitForElement(driver,"NAME","password",60)

password.send_keys(your_password)
email.send_keys(your_mail)
waitForElement(driver,"CLASS","submit",30).click()

waitForElement(driver,"CLASS","grouptab",80)
all_groups = driver.find_elements_by_class_name("grouptab")
visible_groups  = []
StaleElement = True

for group in all_groups:
    if (group.get_attribute("style") == 'display: block;'):
        visible_groups.append({
            "id" : group.get_attribute("id"),
            "name" : group.text,
            })

for grp_id in visible_groups:
    whole_data = []
    waitForElement(driver,"ID",grp_id["id"],30).click()
    filepath = os.path.join("./../"+time.strftime("%d.%m.%Y")+" saves", grp_id["name"])
    chat_file  = open(filepath, "w")
    find_elem = None
    while not find_elem:
        try:
            find_elem = waitForElement(driver,"CLASS","calls-to-action-welcome",1)
            try:
                next_elements = driver.find_elements_by_class_name("post")
                for element in next_elements[::-1]:
                    try:
                        name = element.find_element_by_tag_name("author").get_attribute("innerHTML")
                    except NoSuchElementException:
                        name = "None"
                    timedate = element.find_element_by_class_name("timestamp").get_attribute("innerHTML")
                    text = element.find_element_by_class_name("post_text").get_attribute("innerHTML")
                    if len(text) > 0:
                        whole_data.append({
                            "name" : name,
                            "time" : timedate,
                            "text" : text
                        })
            except:
                whole_data.append({
                    "name": "",
                    "time": "",
                    "text": "NO CONVERSATIONS"
                })
        except:
            if StaleElement:
                driver.execute_script("window.scrollTo(0, -200)")
            try:
                actions = ActionChains(driver)
                actions.move_to_element(waitForElement(driver,"CLASS","post_text",30))
                actions.perform()
                waitForElement(driver,"CLASS","post",30)
                if StaleElement:
                    next_elements = driver.find_elements_by_class_name("post")
                try:
                    for element in next_elements[::-1]:
                        try:
                            name = element.find_element_by_tag_name("author").get_attribute("innerHTML")
                        except NoSuchElementException:
                            name = "None"
                        timedate = element.find_element_by_class_name("timestamp").get_attribute("innerHTML")
                        text = element.find_element_by_class_name("post_text").get_attribute("innerHTML")
                        if len(text) > 0:
                            whole_data.append({
                                "name" : name,
                                "time" : timedate,
                                "text" : text
                            })
                    StaleElement = True
                except StaleElementReferenceException:
                    next_elements = driver.find_elements_by_class_name("post")
                    StaleElement = False
            except TimeoutException as ex:
                print("Thrown exception: ", ex)
    checked = set()
    cleaned_data = []
    for data in whole_data:
        t = tuple(data.items())
        if t not in checked:
            checked.add(t)
            cleaned_data.append(data)
    for data in cleaned_data:
        chat_file.write("\n"+data["name"]+"\t\t\t"+data["time"]+"\n"+data["text"]+"\n")
    chat_file.close()
driver.close()
