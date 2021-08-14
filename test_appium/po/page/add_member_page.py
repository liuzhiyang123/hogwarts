from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.page.base_page import BasePage
from test_appium.po.page.message_record_page import MessageRecordPage


class AddMemberPage(BasePage):

    _input_add_loc=(MobileBy.XPATH, '//*[@text="手动输入添加"]')

    def click_add_member(self):
        self.find_and_click(self._input_add_loc)
        return MessageRecordPage(self.driver)