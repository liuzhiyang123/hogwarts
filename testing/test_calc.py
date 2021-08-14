import pytest
import yaml
from pythoncode.calc import Calc
import os

def get_data(file):
    with open(file) as fp:
        data=yaml.safe_load(fp)
    return data

data=get_data(os.path.join(os.path.abspath(__file__).split('hogwarts')[0],'hogwarts','testing','calc.yml'))

class TestMain:
    def setup_class(self):
        self.calc=Calc()
        print('类开始')

    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize(['a','b','expected'],
                             data['add']['data'],
                             ids=data['add']['ids'])
    def test_add(self,a,b,expected):
        '''测试加方法'''
        assert self.calc.add(a,b)==expected

    @pytest.mark.parametrize(['a', 'b', 'expected'],
                             [(3,2,1), (100, 40,60), (-1,-2,1)],
                             ids=['int', 'max', 'minus'])
    def test_sub(self,a,b,expected):
        '''测试减方法'''
        assert self.calc.sub(a,b)==expected

    @pytest.mark.parametrize(['a', 'b', 'expected'],
                             [(3, 2, 6), (100, 40,4000), (-1, -2, 2)],
                             ids=['int', 'max', 'minus'])
    def test_mul(self,a,b,expected):
        '''测试乘方法'''
        assert self.calc.mul(a,b)==expected

    @pytest.mark.parametrize(['a', 'b', 'expected'],
                             [(3, 2, 1.5), (100, 20,5), (-1, -2, 0.5)],
                             ids=['int', 'max', 'minus'])
    def test_div(self,a,b,expected):
        '''测试除方法'''
        assert self.calc.div(a,b)==expected

if __name__ == '__main__':
    pytest.main(['-sv','test_calc.py'])
