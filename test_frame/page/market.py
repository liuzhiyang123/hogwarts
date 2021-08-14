from selenium.webdriver.common.by import By

from test_frame.base_page import BasePage
from test_frame.page.serach import Search


# 面向对象四大特点
class Market(BasePage):
    def goto_search(self):
        self.find_and_click((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"))
        #self.basepage.load("../page/market.yaml")
        return Search(self.driver)