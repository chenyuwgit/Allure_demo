# __*__coding:utf-8 __*__

import pytest
from common_contion.loging import longin

@pytest.fixture(scope="session")
def login_fixture():
    longin()
    print("这个是前置操作：登录")