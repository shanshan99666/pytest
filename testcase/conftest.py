# conftest
# 2022/10/13
import pytest

from lib.apilib.login import Login
from lib.apilib.myshop import MyShop


@pytest.fixture(scope='session',autouse=True)
def start_demo(request):
    print("包任何运行一个都会执行,可以做预处理")
    def fin():
        print("自动化测试结束,清理东西")
    request.addfinalizer(fin)

@pytest.fixture(scope='function')
def updtainit():
    print("我是类函数初始化")


@pytest.fixture(scope='function')
def getshopidandimage():
    ms = MyShop(Login().login('{"username":"th0198","password":"xintian"}',getToken=True))
    fileid = ms.getUpLoadFilerRealFileName('WechatIMG9293.jpeg')
    shopid = ms.listMyShop({'page':1,'limit':1})['data']['records'][0]['id']
    return shopid,fileid