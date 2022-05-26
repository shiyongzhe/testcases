import xlwt
from entity.params import params

class exportexcel:

    def __init__(self):
        global wb
        wb = xlwt.Workbook(encoding = "ascii")

    def createsheet(self, *args):
        worksheet = wb.add_sheet("casesresult")
        for index in range(len(args)):
            # 获取参数对象信息
            param = args[index][0]
            for cell in range(7):
                worksheet.write(index, cell, str(self.getCellData(param, cell)))
        wb.save("./testcases/result.xls")

    def getCellData(self, p=params, cell=int):
        res = ""
        if cell == 0:
            res = p.caseno
        if cell == 1:
            res = p.casename
        if cell == 2:
            res = p.testname
        if cell == 3:
            res = p.apipath
        if cell == 4:
            res = p.params
        if cell == 5:
            res = p.expectresult
        if cell == 6:
            res = p.actualresult
        if cell == 7:
            res = p.requestmethod
        return res

