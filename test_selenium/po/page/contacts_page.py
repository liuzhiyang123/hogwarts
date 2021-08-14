import time

from selenium.webdriver.common.by import By

from .BasePage import BasePage


class ContactsPage(BasePage):

    def goto_add_member(self):
        from .add_member_page import AddMemberPage
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,'.ww_operationBar .js_add_member').click()
        return AddMemberPage(self.driver)

    def get_member(self):
        elements=self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        return [ele.text for ele in elements]