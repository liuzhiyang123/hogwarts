import random

import pytest

from test_selenium.po.page.main_page import MainPage


class TestAddMember:

    def setup_class(self):
        self.page=MainPage()

    def teardown_class(self):
        self.page.back_main()

    def test_add_member1(self):
        v = random.choices(['值', '大', '壮', '得', '哈', '发', '洋', '阳', '分', '放', '无', '天'], k=2)
        name = '刘' + ''.join(v)
        texts=self.page.goto_add_member().add_member(name).get_member()
        print(texts)
        assert name in texts


if __name__ == '__main__':
    pytest.main(['-sv','test_add_member.py'])
