import time

from selenium.webdriver.common.by import By

from test_selenium.selenium.BaseCase import BaseCase


class TestUserJs(BaseCase):

    def test_1(self):
        self.driver.get('https://www.baidu.com')
        e1=self.driver.execute_script('return document.getElementById("kw")')
        e1.send_keys('selenium测试')
        self.driver.execute_script('return document.getElementById("su")').click()
        e1=self.driver.find_element(By.XPATH,'//*[@id="page"]/div/a[10]')
        # self.driver.execute_script('"arguments[0].scrollIntoView();"',e1)
        e1.click()
        time.sleep(5)

    def test_2(self):
        self.driver.get('https://www.12306.cn/')
        time.sleep(3)
        self.driver.execute_script('document.getElementById("train_date").removeAttribute("readonly")')
        self.driver.execute_script('document.getElementById("train_date").value="2020-08-09"')
        time.sleep(5)