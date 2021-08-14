from requests import Response

from test_frame.app import App
from test_frame.page.main_page import Main


class TestSearch:
    def setup(self):
        self.app = App()
        self.app.start()

    def teardown(self):
        self.app.driver.quit()

    def test_search(self):
        self.app.goto_main_page().goto_market().goto_search().search()
