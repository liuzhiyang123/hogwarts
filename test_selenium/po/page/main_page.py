from selenium.webdriver.common.by import By

from test_selenium.po.page.BasePage import BasePage
from test_selenium.po.page.add_member_page import AddMemberPage
from test_selenium.po.page.contacts_page import ContactsPage


class MainPage(BasePage):

    def goto_add_member(self):
        '''跳转到添加成员页面'''
        self.driver.find_element(By.CSS_SELECTOR,'.ww_indexImg_AddMember').click()
        return AddMemberPage(self.driver)

    def goto_contacts(self):
        '''跳转到通讯录页面
        '''
        self.driver.find_element(By.ID,'menu_contacts').click()
        return ContactsPage(self.driver)

    def back_main(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')