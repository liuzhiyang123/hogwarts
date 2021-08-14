import pytest

@pytest.mark.demo
def test_one():
    print('test one')

@pytest.mark.smoke
@pytest.mark.demo
def test_two():
    print('test two')


if __name__ == '__main__':
    pytest.main(['-sv','test_mark.py'])