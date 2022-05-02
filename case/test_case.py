# __*__coding:utf-8 __*__

import allure
from common_contion.dome_Interface import *
from allure_commons._allure import severity
from allure_commons.types import Severity as severity_level

@allure.severity("blocker")
@allure.epic("项目名称: 测试学习管理系统")
@allure.issue("禅道bug地址-01")  # 禅道bug地址
@allure.testcase("禅道用例连接地址-01")  # 禅道用例连接地址
@allure.feature("财务模块")
class Testdome1(object):
    def test_dome_1(self,login_fixture):
        '''用例一的用例描述: 我是第一个用例，我只有一个步骤'''
        print("第一个测试用例")
        jieko_dome_1()


    def test_dome_2(self,login_fixture):
        '''用例二的用例描述: 我是第二个用例，我只有一个步骤'''
        print("第二个测试用例")
        jieko_dome_2()


@allure.severity("critical")
@allure.epic("项目名称: 测试学习管理系统")
@allure.feature("售后订单模块")
@allure.story("用例的标题: 对资源进行增、删、改、查")
@allure.issue("禅道bug地址-02")  # 禅道bug地址
@allure.testcase("禅道用例连接地址-02")  # 禅道用例连接地址
class Testdome3(object):
    def test_dome_3(self,login_fixture):
        '''用例三的用例描述: 我是第三个用例，我是有多个步骤；'''
        print("第三个测试用例")
        f = jieko_dome_3()
        f.jieko_dome_3_1()
        f.jieko_dome_3_2()
        f.jieko_dome_3_3()
        f.jieko_dome_3_4()