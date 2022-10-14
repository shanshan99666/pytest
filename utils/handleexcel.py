# handleexcel
# 2022/10/12
import xlrd
import xlwt


from utils.logstream import logger


from xlutils.copy import copy

from utils.handlepath import excelpath
class HandleExcel:
    def getExcelData(self,sheetname,casename):
        wb = xlrd.open_workbook(excelpath,formatting_info=True)
        sheet = wb.sheet_by_name(sheetname)
        resqlist = []
        rows = 0
        sheetmaxrow = sheet.col_values(0)
      #  print(sheetmaxrow)
        for i in range(0,len(sheetmaxrow)):
            if casename in sheetmaxrow[i]:
                reqdata = sheet.cell(rows,9).value
                respmsg = sheet.cell(rows,11).value
                resqlist.append((reqdata, respmsg))
            rows += 1
       # print(resqlist)
        return resqlist

    def getIndexBySheetName(self,sheetname):
        wb = xlrd.open_workbook(excelpath)
        sheets = wb.sheet_names()

        for i in range(len(sheets)):
            if sheetname == sheets[i]:
                return i
      #  log.info("获取索引失败")
        return -1


    def setExcelData(self,sheetname):
        wb = xlrd.open_workbook(excelpath,sheetname,formatting_info=True)
        wbNew = copy(wb)
        sheetNew = wbNew.get_sheet(self.getIndexBySheetName(sheetname))
        return (wbNew,sheetNew)



if __name__ == '__main__':
    print(HandleExcel().getExcelData('登录模块','Login'))