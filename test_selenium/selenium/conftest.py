import os

import pytest
import json

def pytest_generate_tests(metafunc):
    print(metafunc.__dir__())
    file=metafunc.module.__file__.replace('.py','.json')
    if os.path.isfile(file):
        with open(file) as fp:
            data=json.load(fp)
    else:
        data={}
    print(metafunc.definition)
    # print(metafunc.parametrize('data',['123']))
    print(metafunc.cls.__name__)
    function_name=metafunc.function.__name__
    default=data.get('default')
    print('default',default)
    if default:
        for key,value in default.items():
            print(key,value)
            if not hasattr(metafunc.cls,key):
                setattr(metafunc.cls,key,value)
    if data.get(function_name):
        metafunc.parametrize('data',data.get(function_name))

