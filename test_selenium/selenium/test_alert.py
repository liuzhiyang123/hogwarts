import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from test_selenium.selenium.BaseCase import BaseCase


class TestUserJs(BaseCase):

    def test_1(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        action=ActionChains(self.driver)
        e1=self.driver.find_element(By.ID,'draggable')
        e2=self.driver.find_element(By.ID,'droppable')
        action.drag_and_drop(e1,e2).perform()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID,'submitBTN').click()
        time.sleep(3)