from appium import webdriver

from test_appium.po.page.base_page import BasePage
from test_appium.po.page.main_page import MainPage


class App(BasePage):

    def start(self):
        caps = {
            'platformName': "Android",
            'platformVersion': "6",
            'deviceName': "vivo x5",
            # 'app': "/path/to/the/downloaded/ApiDemos-debug.apk",
            'appPackage': "com.tencent.wework",
            'appActivity': ".launch.LaunchSplashActivity",  # ".launch.LaunchSplashActivity",
            'automationName': "UiAutomator2",
            'systemPort': '8200',
            'noReset': 'true',
            'skipServerInstalltion': 'true',  # 跳过安装
            'udid': '8f7fb4bc',
            # 'newCommandTimeout': 120,
            'adbExecTimeout': 20000,
            'settings[waitForIdleTimeout]': 0,  # 设置页面等待空闲状态的时间
            'newCommandTimeout': 120
        }
        for i in range(2):
            try:
                self.driver = webdriver.Remote('http://127.0.0.1:4700/wd/hub', caps)
            except Exception as e:
                if i == 1:
                    raise e

    def goto_main_page(self):
        return MainPage(self.driver)
