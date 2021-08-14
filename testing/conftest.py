import pytest
import yaml
import os
import requests

@pytest.fixture(scope='session',params=['***参数1***','***参数2***'],ids=['test1','test2'])
def myfixture(request):
    print('myfixture 传入参数%s'%request.param)
    yield request.param
    print('myfixture结束操作')

def get_datas():
    file=os.path.join(os.path.abspath(os.path.dirname(__name__)).split('hogwarts')[0],
                      'hogwarts',
                      'testing',
                      'calc.yml')
    with open(file) as fp:
        data=yaml.safe_load(fp)
    return data

data=get_datas()

@pytest.fixture(scope='module',params=data['add']['data'],ids=data['add']['ids'])
def add_fixture(request):
    yield request.param
    print('fixture calc执行结束')

@pytest.fixture(scope='module',params=data['div']['data'],ids=data['div']['ids'])
def div_fixture(request):
    yield request.param


def pytest_generate_tests(metafunc):
    print('metafunc',metafunc.module.__file__,metafunc.cls,metafunc.function.__name__)
    # print(metafunc.parametrize())

def pytest_collection_modifyitems(session,config,items):
    for item in items:
        # print('item',item.nodeid,item.fspath,item.function.__doc__)
        description=f'path:{item.fspath.strpath};'
        doc=item.function.__doc__.strip().strip('\n').strip() if item.function.__doc__ else 'null'
        description+=f'注释:{doc}'
        rj=requests.post('http://127.0.0.1:5000/testcase_store',json={
            'nodeid':item.nodeid,
            'description': description
        })
        print(rj.text)