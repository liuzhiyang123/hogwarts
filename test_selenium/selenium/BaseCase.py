from selenium import webdriver


class BaseCase:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()