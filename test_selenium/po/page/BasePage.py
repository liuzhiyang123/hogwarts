import yaml
from selenium import webdriver


class BasePage:

    def __init__(self, driver:webdriver.Chrome = None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(20)
            self._cookie_login()
        else:
            self.driver = driver

    def _cookie_login(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?'
                        'redirect_uri=https://work.weixin.qq.com/wework_admin/frame')
        with open('data.yml') as fp:
            data = yaml.safe_load(fp)
        for d in data:
            self.driver.add_cookie(d)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
