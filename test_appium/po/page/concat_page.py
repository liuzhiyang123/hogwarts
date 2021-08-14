from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.page.add_member_page import AddMemberPage
from test_appium.po.page.base_page import BasePage


class ConcatPage(BasePage):

    def goto_add_member(self):
        self.swipe_find((MobileBy.XPATH,'//*[@text="添加成员"]')).click()
        return AddMemberPage(self.driver)