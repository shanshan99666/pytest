# handlepath
# 2022/10/12

import os

curpath = os.path.abspath(__file__)

projectpath = os.path.dirname(os.path.dirname(curpath))

excelpath = projectpath + '/data/Delivery_System_V1.5.xls'

resultpath = projectpath + '/data/Delivery_System.xls'

datapath = projectpath + '/data'

reportpath = projectpath + '/outfiles/reports'

yamlpath = projectpath + '/configs/config.yaml'