# test_login
# 2022/10/12
import json
import os
import pytest
from utils.handleexcel import HandleExcel
from lib.apilib.login import Login
class TestLogin:
    @pytest.mark.parametrize('excelreqbody,excelexpresponse',HandleExcel().getExcelData('登录模块','Login'))

    def test_login(self,excelreqbody,excelexpresponse):
        realresponse = Login().login(excelreqbody,False) ###易错,没有实例化.......
        tmp = excelexpresponse
        tmp2 = realresponse['msg']
        assert realresponse['msg'] == json.loads(excelexpresponse)['msg']


if __name__ == '__main__':
    pytest.main(['test_login.py', '-s', '--alluredir', '../outfiles/reports/tmp'])
    os.system('allure serve ../outfiles/reports/tmp')