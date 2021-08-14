import time

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestMiniProgram:

    def setup(self):
        caps = {
            'platformName': 'android',
            'deviceName': 'vivox23',
            'platfromVersion': '9',
            'chromedriverExecutable': '/Users/liuzy/Desktop/package/chromedriver_2_14',
            # 'appPackage': "com.tencent.mm",
            # 'appActivity': "com.tencent.mm.ui.LauncherUI",
            'adbPort': 5038
        }
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)

    def teardown(self):
        pass

    def write(self,file,content):
        with open(file,'w') as fp:
            fp.write(''.join(content))

    def test_api(self):
        time.sleep(5)
        #self.driver.make_gsm_call('13310155819',GsmCallActions.CALL)
        #self.driver.send_sms('13310155819','这是一条短信')
        self.driver.start_recording_screen()
        content=self.driver.get_log('logcat')
        content=''.join([f"{c['timestamp']}:{c['message']}" for c in content])
        time.sleep(5)
        self.write('123.log',content)
        self.driver.stop_recording_screen()
        #self.write('driver.log',content)
        #content=self.driver.get_log('bugreport')
        #print(content)
        #self.write('client.log',content)