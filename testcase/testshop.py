# testshop
# 2022/10/13
import json

from lib.apilib.login import Login
from lib.apilib.myshop import MyShop
from utils.handleexcel import HandleExcel


class TestShop:
    def showshop(self):
        token = Login().login('{"username":"th0198","password":"xintian"}',getToken=True)
        data = HandleExcel().getExcelData('我的商铺', 'listshopping')
    #    print(data)
        for i in range(len(data)):
            excelreqbody, excelexpresponse = data[i][0], data[i][1]
            indata = json.loads(excelreqbody)
            print(indata)
            res = MyShop(token).listMyShop(indata)





if __name__ == '__main__':
    TestShop().showshop()