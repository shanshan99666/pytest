# testlogin
# 2022/10/12
# test_login
# 2022/10/12
import json
import os
import pytest
from utils.handleexcel import HandleExcel
from lib.apilib.login import Login
class test:
    def test_login(self):
     data = HandleExcel().getExcelData('登录模块','Login')
     print(data)
     for i  in range(len(data)) :
        excelreqbody,excelexpresponse = data[i][0],data[i][1]
        realresponse = Login.login(excelreqbody,False)
        tmp = excelexpresponse
        tmp2 = realresponse['msg']
        if realresponse['msg'] == json.loads(excelexpresponse)['data']['msg']:
            print("pass")
        else:
            print("fail")
if __name__ == '__main__':
    test().test_login()
