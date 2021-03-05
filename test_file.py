import pytest
import allure
import os
from PIL import Image

@allure.feature('测试模块')
class TestFile:

    @allure.story('测试场景')
    def test_img(self):
        fp=open('img.png','rb')
        allure.attach(fp.read(), name='图片',attachment_type=allure.attachment_type.PNG)
        allure.attach.file('video.mp4', name='军舰', attachment_type=allure.attachment_type.MP4)
        with allure.step('1.步骤1：哈哈哈'):
            pass
        allure.attach('为了科学','哈哈')


if __name__ == '__main__':
    os.system('pytest -sv --alluredir=xml test_file.py --clean-alluredir')
    os.system('allure generate xml -o html --clean')