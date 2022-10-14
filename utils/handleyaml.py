# handleyaml
# 2022/10/14
import yaml
from utils.handlepath import yamlpath

def getYamlData(filedir):
    f = open(filedir,'r',encoding='utf-8')
    res = yaml.load(f)
    print(res)

if __name__ == '__main__':
    getYamlData(yamlpath)