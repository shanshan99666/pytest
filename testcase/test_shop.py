# test_shop
# 2022/10/13
import os

import allure
import pytest

from lib.apilib.login import Login
from lib.apilib.myshop import MyShop
from utils.handleemail import send_mail
from utils.handleexcel import HandleExcel
import json
import os
from utils.handlepath import  reportpath
@allure.epic("商店")
@allure.feature("测试我的商铺")
@pytest.mark.shop
class Test_Myshop:
    def setup_class(self):
        self.token = Login().login('{"username":"th0198","password":"xintian"}',getToken=True)
        print('setup初始化,只执行一次')
    @allure.story("列出商铺")
    @allure.title("商铺测试用例")
    @pytest.mark.list_shop
    @pytest.mark.parametrize('excelreqbody,excelexpresponse',HandleExcel().getExcelData('我的商铺','listshopping'))
    @pytest.mark.usefixtures('updtainit')
    def test_list_myshop(self,excelreqbody,excelexpresponse):

        res = MyShop(self.token).listMyShop(json.loads(excelreqbody))

        exp = json.loads(excelexpresponse)
      #  print(res)
        if 'code' in res and 'code' in exp:
             assert res['code'] == exp['code']
        else:
             assert res['error'] == exp['error']
    @pytest.mark.modifyshop
    @pytest.mark.parametrize('exr,exb',HandleExcel().getExcelData('我的商铺','updateshopping'))
    def test_modifyshop(self,exr,exb,getshopidandimage):
        shopid = getshopidandimage[0]
        fileid = getshopidandimage[1]
        res = MyShop(self.token).modifyShop(json.loads(exr),shopid,fileid)
        # if res['code'] == json.loads(exb)['code']:
        #     print("111")
        assert res['code'] == json.loads(exb)['code']



if __name__ == '__main__':

    for i in os.listdir(f'{reportpath}/tmp'):
        if 'json' in i:
            os.remove(f'{reportpath}/tmp/{i}')

    pytest.main(['test_shop.py', '-s', '-m','shop','--alluredir', '../outfiles/reports/tmp'])
    os.system('allure serve ../outfiles/reports/tmp')
    send_mail("Liang.Wu@test.com", "api测试报告", "测试报告的访问地址为：http://desktop-fe56ou7:8881/index.html<br> 请在收到邮件后三十分钟内查看！")

