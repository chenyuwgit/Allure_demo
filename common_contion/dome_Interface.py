# __*__coding:utf-8 __*__

import allure

def jieko_dome_1():
    '''用例描述: 用例一的接口'''
    print("这个是第一个用例对应的接口")

def jieko_dome_2():
    '''用例描述: 用例二的接口'''
    print("这个是第二个用例对应的接口")


@allure.feature("资源管理模块")
class jieko_dome_3(object):
    '''这个是一个模块的测试'''
    @allure.step("操作步骤: 新增资源个人信息")
    def jieko_dome_3_1(self):
        '''用例描述: 用例三的新增内容接口'''
        print("这个是第三个用例对应的接口一")

    @allure.step("操作步骤: 查询资源在线信息")
    def jieko_dome_3_2(self):
        '''用例描述: 用例三的查询内容接口'''
        print("这个是第三个用例对应的接口二")

    @allure.step("操作步骤: 修改资源身份信息")
    def jieko_dome_3_3(self):
        '''用例描述: 用例三的编辑内容接口'''
        print("这个是第三个用例对应的接口三")

    @allure.step("操作步骤: 删除资源全部信息")
    def jieko_dome_3_4(self):
        '''用例描述: 用例三的删除内容接口'''
        print("这个是第三个用例对应的接口四")
