import pytest


def add(a:int,b:int)->int:
    return a+b

@pytest.mark.parametrize(['a','b','expected'],
                         [(1,2,3),(3,4,7),(-1,-2,-3),(101,102,200)],
                         ids=['min','mid','-','big'])
def test_param(a,b,expected):
    '''
    参数化测试
    '''
    assert add(a,b)==expected

@pytest.mark.parametrize('a',[1,2])
@pytest.mark.parametrize('b',[3,4])
def test_param2(a,b):
    print('测试参数a->%i,b->%i'%(a,b))

if __name__ == '__main__':
    pytest.main(['-sv','test_param.py::test_param2'])