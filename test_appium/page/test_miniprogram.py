from appium import webdriver


class TestMiniProgram:

    def setup(self):
        caps = {
            'platformName': 'android',
            'deviceName': 'vivox23',
            'platfromVersion': '5.1.1',
            'chromedriverExecutable': '/Users/liuzy/Desktop/package/chromedriver_2_14',
            'appPackage': "com.tencent.mm",
            'appActivity': "com.tencent.mm.ui.LauncherUI"
        }
        caps['chromeOption'] = {
            'androidProcess':'com.tencent.mm:appbrand0'
        }
        caps['adbPort']='5038'
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)

    def teardown(self):
        pass

    def find_top_window(self):
        for window in self.driver.window_handles:
            if ':VISIBLE' in self.driver.title:
                break
            else:
                self.driver.switch_to(window)

    def test_miniprogram(self):
        pass