import random
import string
import time
import inspect
from selenium.webdriver.common.by import By

from test_selenium.po.page.BasePage import BasePage
from test_selenium.po.page.contacts_page import ContactsPage


class AddMemberPage(BasePage):

    def add_member(self,name):
        time.sleep(1)
        self.driver.find_element(By.ID, 'username').send_keys(name)
        v = random.choices(string.ascii_lowercase, k=10)
        self.driver.find_element('id', 'memberAdd_acctid').send_keys(''.join(v))
        v = ''.join([str(i) for i in random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], k=4)])
        self.driver.find_element('id', 'memberAdd_phone').send_keys('1331045' + v)
        self.driver.find_element(By.NAME, 'sendInvite').click()
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        self.driver.find_element(By.ID,'menu_contacts').click()
        # if inspect.stack()
        return ContactsPage(self.driver)
