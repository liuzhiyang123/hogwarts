import pytest
from pythoncode.calc import Calc


class TestFixtureCalc:

    def test_add(self, add_fixture):
        '''套件yield参数话测试add'''
        assert Calc().add(add_fixture[0], add_fixture[1]) == add_fixture[2]

    def test_div(self, div_fixture):
        '''套件yield参数化测试div'''
        assert Calc().div(div_fixture[0], div_fixture[1]) == div_fixture[2]


if __name__ == '__main__':
    pytest.main(['-sv', 'test_fixture_calc.py'])
