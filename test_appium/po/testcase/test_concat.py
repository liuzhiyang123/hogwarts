from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_appium.po.page.app import App


class TestConcat:

    def setup(self):
        self.app=App()
        self.app.start()

    def teardown(self):
        self.app.driver.quit()

    def test_wework(self):
        loc=self.app.goto_main_page().goto_concat().\
            goto_add_member().click_add_member().\
            add_member_message().is_in_page('手动输入添加')