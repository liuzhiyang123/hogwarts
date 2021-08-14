from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

option=webdriver.ChromeOptions()
option.add_experimental_option('w3c',False)
driver = webdriver.Chrome(options=option)



def find_element(loc,timeout=10,per=0.5)->WebElement:
    try:
        return WebDriverWait(driver,timeout,per).until(ec.presence_of_element_located(loc))
    except:
        print(loc,'元素未找到')
        raise

driver.get('https://www.baidu.com')

find_element((By.ID,'kw')).send_keys('霍格沃滋学院')
find_element((By.ID,'su')).click()