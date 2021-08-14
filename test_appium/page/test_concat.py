import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWework:

    def setup(self):
        caps = {
            'platformName': "Android",
            'platformVersion': "6",
            'deviceName': "vivo x5",
            # 'app': "/path/to/the/downloaded/ApiDemos-debug.apk",
            'appPackage': "com.tencent.wework",
            'appActivity': ".launch.LaunchSplashActivity",  # ".launch.LaunchSplashActivity",
            # 'automationName': "UiAutomator2",
            # 'systemPort': '8200',
            'noReset': 'true',
            'skipServerInstalltion': 'true',  # 跳过安装
            'udid': '8f7fb4bc',
            # 'newCommandTimeout': 120,
            'adbExecTimeout': 20000,
            'settings[waitForIdleTimeout]': 0,  # 设置页面等待空闲状态的时间
        }
        for i in range(2):
            try:
                self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            except Exception as e:
                if i == 1:
                    raise e
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wework(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 滚动查找元素
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        flag=WebDriverWait(self.driver,10).until(lambda x:'完整输入' in x.page_source)
        if flag:
            self.driver.find_element(MobileBy.XPATH, '//*[@text="完整输入"]').click()
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text,"姓名")]/following-sibling::*[@text="必填"]').send_keys('张三')
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text,"帐号")]/following-sibling::*[@text="选填"]').send_keys('12345')
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text,"手机")]/../*[@text="手机号"]').send_keys('11213310150')
        self.driver.find_element(MobileBy.XPATH,'//*[@text="保存"]').click()