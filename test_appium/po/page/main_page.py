from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.page.base_page import BasePage
from test_appium.po.page.concat_page import ConcatPage


class MainPage(BasePage):

    def goto_concat(self):
        self.find_and_click((MobileBy.XPATH, '//*[@text="通讯录"]'))
        return ConcatPage(self.driver)