from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.page.base_page import BasePage


class MessageRecordPage(BasePage):

    def add_member_message(self):
        flag = self.is_in_page('完整输入')
        if flag:
            self.find_and_click((MobileBy.XPATH, '//*[@text="完整输入"]'))
        self.find_and_send((MobileBy.XPATH,
                                 '//*[contains(@text,"姓名")]/following-sibling::*[@text="必填"]'),'张三')
        self.find_and_send((MobileBy.XPATH,
                                 '//*[contains(@text,"帐号")]/following-sibling::*[@text="选填"]'),'12345')
        self.find_and_send((MobileBy.XPATH,
                                 '//*[contains(@text,"手机")]/../*[@text="手机号"]'),'11213310150')
        self.swipe_find((MobileBy.XPATH, '//*[@text="保存"]')).click()
        from test_appium.po.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)