import os

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts:

    def test_hogwarts1(self,data):
        print(self.e1,self.e2)
        # driver=webdriver.Chrome()
        # driver.implicitly_wait(5)
        # driver.get('https:www.baidu.com')
        # driver.find_element(By.ID,'kw').send_keys('霍格沃滋测试学院')
        # driver.find_element(By.ID,'su').click()
        # driver.find_element(By.LINK_TEXT,'霍格沃兹测试学院 - 主页')
        print('test_hogwarts',data)


if __name__ == '__main__':
   import pytest
   pytest.main(['-sv','test_hogwarts.py'])