# myfile
# 2022/10/14
import requests
import pprint


def uploadfile():
    url = 'https://main.test.com/storage/1/storage?dir=abc'
    file = {
        'file': open('/Users/zhangyang/PycharmProjects/untitled/image/yinzhang.png', 'rb')
    }
    header = {
        'token': 'token'
    }

    ret = requests.post(url=url, files=file, headers=header, verify=False)
    pprint.pprint(ret.json())



""""
file = {
    'file': ('yinzhang.png', open('/Users/zhangyang/PycharmProjects/untitled/image/yinzhang.png', 'rb'))
}

file = {
    'file': ('yinzhang.png', open('/Users/zhangyang/PycharmProjects/untitled/image/yinzhang.png', 'rb'), 'image/png')
}
"""

def downloadfile():
    download_url = 'https://main-test.3hea.com/web/1/report/'  # 下载链接
    ret = requests.get(url=download_url, headers=headers)
    with open('aaa.xlsx', 'wb') as f:  # 将返回的数据写入文件
        f.write(ret.content)