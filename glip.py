from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import collections

class OrderedSet(collections.MutableSet):

    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)
        
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
group_ids, group_names, visible_groups, texts, first_texts = [], [], [], [], []

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
    first_elemets = driver.find_elements_by_class_name("post_text")
    for element in first_elemets:
        first_texts.append(element.get_attribute("innerHTML"))
    while not find_elem:
        try:
            find_elem = waitForElementClassNameShort(driver,"calls-to-action-welcome")
        except:
            try:
                actions = ActionChains(driver)
                actions.move_to_element(waitForElementClassName(driver,"post_text"))
                actions.perform()
                texts = driver.find_elements_by_class_name("post_text")
                for text in texts:
                    first_texts.append(text.get_attribute("innerHTML"))
                    first_texts = list(OrderedSet(first_texts))
                driver.execute_script("window.scrollTo(0, -200)")
                waitForElementClassName(driver,"post_text")
            except TimeoutException as ex:
                print("Thrown exception: ", ex)
    for textaz in first_texts:
        print(textaz)
        
''' 
   for text in texts:  
        for tex in text:      
            text_value = tex.get_attribute('innerHTML')
            print(text_value)
'''
