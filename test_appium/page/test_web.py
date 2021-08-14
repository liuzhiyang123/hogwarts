import time

import pytest
from appium import webdriver


class TestWeb:

    def setup(self):
        caps = {
            'platformName': 'android',
            'deviceName': 'vivox23',
            'platfromVersion': '5.1.1',
            'chromedriverExecutable': '/Users/liuzy/Desktop/package/chromedriver_2_14',
            #'chromedriverExecutableDir':'/Users/liuzy/Desktop/package',
            'browserName': 'browser',
            #'skipServerInstalltion': 'true'
        }
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities=caps)

    def teardown(self):
        self.driver.quit()

    def test_web(self):
        self.driver.get('https://m.baidu.com')
        time.sleep(5)

    @pytest.mark.skip()
    def test_sougou(self):
        self.driver.get('https://sougou.com')
        time.sleep(2)
