import pytest


class TestDemo:
    def test_one(self,myfixture):
        env=myfixture
        print('test_one传入myfixture变量%s'%env)
        print('开始执行***test_one***')

    def test_two(self,myfixture):
        nv = myfixture
        print('test_two传入myfixture变量%s' % nv)
        print('开始执行***test_two***')


if __name__ == '__main__':
    pytest.main(['-sv','test_fixture.py'])