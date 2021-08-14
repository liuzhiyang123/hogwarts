import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_frame.black_handle import black_handle


class BasePage:
    FIND = 'find'
    ACTION = 'action'
    FIND_AND_CLICK = 'find_and_click'
    SEND = 'send'
    CONTENT = 'content'

    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    @black_handle()
    def find(self, loc: tuple, timeout=8, is_visible=False, is_click=False) -> WebElement:
        if is_click:
            method = EC.element_to_be_clickable(loc)
        elif is_visible:
            method = EC.visibility_of_element_located(loc)
        else:
            method = EC.presence_of_element_located(loc)
        ele = WebDriverWait(self.driver, timeout=timeout).until(method)
        return ele

    def finds(self, loc, timeout=8, is_visible=False):
        if is_visible:
            method = EC.visibility_of_all_elements_located(loc)
        else:
            method = EC.presence_of_all_elements_located(loc)
        try:
            elements = WebDriverWait(self.driver, timeout=timeout).until(method)
            return elements
        except:
            return []

    def find_and_click(self, loc, timeout=8):
        self.find(loc, timeout, is_click=True).click()

    def find_and_send(self, loc, text, timeout=8):
        self.find(loc, timeout, is_click=True).send_keys(text)

    def swipe_find(self, loc, director='up', swipe_per=0.6, swipe_times=5, timeout=3, duration=1000):
        for i in range(swipe_times):
            try:
                ele = self.find(loc, timeout=timeout, is_visible=True)
                return ele
            except Exception as e:
                if i == swipe_times - 1:
                    raise e
                else:
                    self.swipe(director, swipe_per, duration)

    def swipe(self, director='up', swipe_per=0.6, duration=1000):
        '''
        start_x: x-coordinate at which to start
        start_y: y-coordinate at which to start
        end_x: x-coordinate at which to stop
        end_y: y-coordinate at which to stop
        duration: time to take the swipe, in ms.
        '''
        size = self.driver.get_window_size()
        width, height = size['width'], size['height']
        if director == 'up':
            start_x = end_x = 0.5 * width
            start_y = height * 0.5 + height * swipe_per * 0.5
            end_y = height * 0.5 - height * swipe_per * 0.5
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def is_in_page(self, text, timeout=3) -> bool:
        try:
            return WebDriverWait(self.driver, timeout).until(lambda x: text in x.page_source)
        except TimeoutException as e:
            return False

    def load(self, yaml_path):
        with open(yaml_path, encoding="utf-8") as f:
            data = yaml.load(f)
        for step in data:
            xpath_expr = step.get(self.FIND)
            action = step.get(self.ACTION)
            if action == self.FIND_AND_CLICK:
                self.find_and_click((By.XPATH, xpath_expr))
            elif action == self.SEND:
                content = step.get(self.CONTENT)
                self.find_and_send((By.XPATH, xpath_expr), content)