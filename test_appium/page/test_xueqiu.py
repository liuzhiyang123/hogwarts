from appium import webdriver

class TestXueQiu:

    def setup(self):
        desired_caps = {
            'platformName': "Android",
            'platformVersion': "8",
            'deviceName': "d",
            'appPackage': "com.xueqiu.android",
            'appActivity': "com.xueqiu.android.common.splash.SplashActivity",
            #'appWaitActivity':"com.xueqiu.android.main.view.MainActivity",
            'automationName': "UiAutomator2",
            'systemPort': '8200',
            'noReset': 'true',
            'skipServerInstalltion': 'true',  # 跳过安装
            'udid': '8f7fb4bc',
            'newCommandTimeout': 120
        }

        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    def teardown(self):
        self.driver.quit()

    def test_xue(self):
        print(self.driver.page_source)