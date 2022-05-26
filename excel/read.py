import xlrd
from entity.params import params

class readexcel:

    def __init__(self):
        global data
        data = xlrd.open_workbook("./testcases/cases.xls")

    def start_read(self):
        # 读取sheets
        table = data.sheets()[0]
        # 获取rows 行
        nrows = table.nrows
        # 获取所有的cells 列
        ncols = table.ncols
        # 初始化返回数组
        list = []
        if nrows > 0:
            for row in range(1, nrows):
                p = params()
                for col in range(0, ncols):
                    # 获取第一行的标题数据
                    title = str(table.cell_value(0, col)).split("/", 1)
                    readdata = str(table.cell_value(row, col))
                    self.build_entity(title[1].strip(), p, readdata)
                list.append(p)
        return list

    def build_entity(self, title=str, p=params, readdata=str):
        if title == "caseNo":
            p.caseno = readdata
        if title == "caseName":
            p.casename = readdata
        if title == "testName":
            p.testname = readdata
        if title == "apiPath":
            p.apipath = readdata
        if title == "params":
            p.params = readdata
        if title == "expectResult":
            p.expectresult = readdata
        if title == "actualResult":
            p.actualresult = readdata
        if title == "requestMethod":
            p.requestmethod = readdata

        return p