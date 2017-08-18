from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
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
        
def waitForElement(drive,element_type,element,wait_time):
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

driver = webdriver.Chrome("../new_hodoor/Hodoor/node_modules/chromedriver/lib/chromedriver/chromedriver")
driver.get('https://glip.com/')
    
waitForElement(driver,"ID","sign_in",30).click()
email = waitForElement(driver,"NAME","email",30)
password = waitForElement(driver,"NAME","password",30)


password.send_keys("MoT159357")
email.send_keys("tomas.houfek@eledus.cz")
waitForElement(driver,"CLASS","submit",30).click()

waitForElement(driver,"CLASS","grouptab",30)
all_groups = driver.find_elements_by_class_name("grouptab")
visible_groups, texts, all_data  = [], [], []
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
    print(grp_id["name"])
    find_elem = None
    try:
        waitForElement(driver,"CLASS","post",30)
        first_elemets = driver.find_elements_by_class_name("post")
        for element in first_elemets:
            name = element.find_element_by_tag_name("author").get_attribute("innerHTML")
            timedate = element.find_element_by_class_name("timestamp").get_attribute("innerHTML")
            text = element.find_element_by_class_name("post_text").get_attribute("innerHTML")
            whole_data.append({
                "name" : name,
                "time" : timedate,
                "text" : text
            })
    except TimeoutException as ex:
        print("Thrown exception: ", ex)
    while not find_elem:
        try:
            find_elem = waitForElement(driver,"CLASS","calls-to-action-welcome",1)
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
                    for element in next_elements:
                        try:
                            name = element.find_element_by_tag_name("author").get_attribute("innerHTML")
                        except NoSuchElementException:
                            name = "Noone"
                        timedate = element.find_element_by_class_name("timestamp").get_attribute("innerHTML")
                        text = element.find_element_by_class_name("post_text").get_attribute("innerHTML")
                        if len(text) >= 0:
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
    all_data+=whole_data
    for data in whole_data:
        print(data["name"],"\t\t\t",data["time"],"\n",data["text"])
    time.sleep(10)
''' 
   for text in texts:  
        for tex in text:      
            text_value = tex.get_attribute('innerHTML')
            print(text_value)

                    for author in authors:
                        waitForElementTagName(driver, "author")
                        print(author.get_attribute("innerHTML"))
                    for timedate in times:
                        waitForElementClassName(driver, "timestamp")
                        print(timedate.get_attribute("innerHTML"))
                    
                    for text in texts:
                        waitForElementClassName(driver, "post_text")
                        print(text.get_attribute("innerHTML"))
                        '''
