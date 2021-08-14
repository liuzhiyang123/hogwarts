import string
import time
import random
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWework:

    def test_cookie(self):
        driver=webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?'
                   'redirect_uri=https://work.weixin.qq.com/wework_admin/frame')
        with open('data.yml') as fp:
            cookies=yaml.safe_load(fp)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get('https://work.weixin.qq.com/wework_admin/frame')
        driver.find_element('id','menu_contacts').click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,'.ww_operationBar .js_add_member').click()
        v=random.choices(['值','大','壮','得','哈','发','洋','阳','分','放','无','天'],k=2)
        #time.sleep(2)
        driver.find_element(By.ID,'username').send_keys('刘'+v[0])
        v=random.choices(string.ascii_lowercase,k=10)
        driver.find_element('id','memberAdd_acctid').send_keys(''.join(v))
        v=random.choices([1,2,3,4,5,6,7,8,9,0],k=4)
        driver.find_element('id','memberAdd_phone').send_keys('1331045'+str(v))
        driver.find_element(By.NAME,'sendInvite').click()
        driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        time.sleep(2)
        driver.quit()