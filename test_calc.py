import pytest
from pythoncode.calc import Calc

class TestMain:
    def setup_class(self):
        self.calc=Calc()
        print('类开始')

    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize(['a','b','expected'],
                             [(1,2,3),(100,200,300),(-1,-2,-3)],
                             ids=['int','max','minus'])
    def test_add(self,a,b,expected):
        assert self.calc.add(a,b)==expected

if __name__ == '__main__':
    pytest.main(['-v','test_calc.py'])
