# logger
# 2022/10/12
import logging
from utils.handlepath import projectpath

def logger():
    #日志器,格式器,输出器
    mylogger = logging.getLogger()
    mylogger.setLevel(logging.INFO)

    fmt = '%(asctime)s %(filename)s %(levelname)s %(module)s %(funcName)s %(message)s'
    frmtor = logging.Formatter(fmt)

    filehandle = logging.FileHandler(f'{projectpath}/outfiles/log/my.log',encoding='utf-8')
    filehandle.setFormatter(frmtor)

    mylogger.addHandler(filehandle)
    return mylogger
