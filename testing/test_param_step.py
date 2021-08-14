import pytest
import yaml


def step1():
    print('开始')

def step2():
    print('注册')

def step3():
    print('登陆')

def steps(file):
    with open(file) as fp:
        _steps=yaml.safe_load(fp)
    for step in _steps:
        if 'step1' in step:
            step1()
        if 'step2' in step:
            step2()
        if 'step3' in step:
            step3()

def test_param_step():
    steps('steps.yaml')

if __name__ == '__main__':
    pytest.main(['-sv','test_param_step.py'])