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
            #'automationName': "UiAutomator2",
            #'systemPort': '8200',
            'noReset': 'true',
            'skipServerInstalltion': 'true',  # 跳过安装
            'udid': '8f7fb4bc',
            #'newCommandTimeout': 120,
            'adbExecTimeout': 20000,
            'settings[waitForIdleTimeout]': 0,  # 设置页面等待空闲状态的时间
        }
        for i in range(2):
            try:
                self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            except Exception as e:
                if i==1:
                    raise e
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wework(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        # 滚动查找元素
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID,'com.tencent.wework:id/guo'))).click()
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((MobileBy.XPATH,'//*[contains(@text,"次外出")]'))).click()
        r = WebDriverWait(self.driver, 10).until(lambda x: '外出打卡成功' in x.page_source)
        print('是否在页面：', r)
