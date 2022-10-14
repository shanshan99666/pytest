# myshop
# 2022/10/12
import requests
from configs.config import Host
from lib.apilib.login import Login

from utils.handlepath import datapath
import pprint
class MyShop:
    def __init__(self,indata):
        self.headers = {'Authorization':indata} #注意看参数格式
    def listMyShop(self,indata):
        url = f'{Host}/shopping/myShop'
        resq = requests.get(url = url,params = indata,headers=self.headers)
        return resq.json()

    def getUpLoadFilerRealFileName(self,filename):
        url = f'{Host}/file'
        filepath = f'{datapath}/{filename}'
        print(filepath)
        uploadfile = {'file':(filename,open(filepath,'rb'),'image/png')}
        resq = requests.post(url=url, headers=self.headers,files = uploadfile)
        return resq.json()['data']['realFileName']

    #indata包括 shopid和图片信息需要获取
    def modifyShop(self,indata,shopid,image):
        url = f'{Host}/shopping/updatemyshop'
        data = indata
        data['id'] = shopid
        data['image'] = f'http://121.41.14.39:8082/file/getImgStream?fileName={image}'
        resq = requests.post(url=url,headers=self.headers,params=data)
        return resq.json()

if __name__ == '__main__':
        str = '{"username":"th0198","password":"xintian"}'
        Authorization = Login().login(str)
# # #    # print(Authorization)
        ms = MyShop(Authorization)
        tmp2 = {'page':1,'limit':0} #要用 tmp2,因为抓包发现请求头要求的是 json 格式
#
        tmp = '{"page":1,"limit":0}'
        pprint.pprint(ms.listMyShop(tmp))
        shopid = ms.listMyShop(tmp2)['data']['records'][0]['id']
        fileid = ms.getUpLoadFilerRealFileName('WechatIMG9293.jpeg')


