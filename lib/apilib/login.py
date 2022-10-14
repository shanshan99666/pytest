#coding=utf-8
# login
# 2022/10/12
import requests
import json
from configs.config import Host

from utils.handleexcel import HandleExcel
import hashlib
import os
from utils.logstream import logger
from utils.handlepath import resultpath
log = logger()

def get_md5_data(pwd: str, salt=''):
    md5 = hashlib.md5()
    # 2-调用加密方法
    pwd = pwd + salt  # 拼接盐值
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()

class Login:
    def login(self,indata,getToken = True):
        url = f"{Host}/account/sLogin"
        indata = json.loads(indata)
        indata['password'] = get_md5_data(indata['password'])
        res = requests.post(url= url,params=indata)
        rescontent = res.json()
       # print(rescontent)
        if getToken:
            try:
                return rescontent['data']['token']
            except:
                log.info("获取token 失败")
                return None
        else:
            return rescontent



# if __name__ == '__main__':
#    # str = '{"username":"th0198","password":"c607d58e3618832f937d80d500a6046c"}'
#     data = HandleExcel().getExcelData('登录模块')
#     wb, sheet = HandleExcel().setExcelData('登录模块')
# #excelreqbody, excelexpresponse
#     rows = 1
#     for i in range(0,len(data)):
#         realresponse = Login().login(data[i][0], False)
#        # print(realresponse)
#        # print(data[i])
#         # print(type(realresponse))
#       #  print(realresponse[i])
#
#         if realresponse['msg'] == json.loads(data[i][1])['msg']:
#             print("pass")
#             sheet.write(rows,12,"pass")
#         else:
#             print("fail")
#             sheet.write(rows,12,"fail")
#         rows += 1
#
#     wb.save(resultpath)

