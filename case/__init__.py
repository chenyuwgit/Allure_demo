# import os
# import pytest
# import allure
#
#
# @allure.feature('feature测试需求001：用户注册')  # 大需求
# @allure.story('story测试场景001：微信用户注册')  # 子需求
# @allure.title('title测试用例001：通过微信正常注册男用户')  # 自定义用例的名称
# def test_case01():
#     assert 1 == 1
#
#
# @allure.feature('feature测试需求001：用户注册')
# @allure.story('story测试场景002：微信用户注册')
# @allure.title('title测试用例002：通过微信正常注册女用户')
# def test_case02():
#     assert 1 == 1
#
#
# @allure.feature('feature测试需求001：用户注册')
# @allure.story('story测试场景003：微信用户注册校验')
# @allure.title('title测试用例003：用户名为空提交注册')
# def test_case03():
#     assert 1 == 3
#
#
# @allure.feature('feature测试需求001：用户注册')
# @allure.story('story测试场景003：微信用户注册校验')
# @allure.title('title测试用例004：密码为空提交注册')
# def test_case04():
#     assert 1 == 4
#
#
# @allure.feature('feature测试需求001：用户注册')
# @allure.story('story测试场景003：微信用户注册校验')
# @allure.title('title测试用例005：用户名存在特殊字符')
# def test_case05():
#     assert 1 == 5
#
# @allure.feature('feature测试需求001：用户注册')
# @allure.story('story测试场景003：微信用户注册校验')
# @allure.title('title测试用例005：用户名超长提交用户信息')
# def test_case06():
#     assert 1 == 6
#
#
# if __name__ == '__main__':
#     pytest.main(['test_allure.py', '--alluredir', './result'])
#     os.system('allure generate ./result/ -o ./report_allure --clean')