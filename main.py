# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import  pytest
import  os

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    #pytest  D:\python-workpase\Allure_demo\case\test_case.py --alluredir=reopore/allure_row_1
    pytest.main(['-vs', './test_case.py::Testdome3', '--alluredir', './reopore/xml'])
    os.system('allure gengerate ./reopore/xml -o ./allreport --clean')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
#allure serve reopore/allure_row_1
#pytest  D:\python-workpase\Allure_demo\case\test_case.py --alluredir=reopore/allure_row_1
