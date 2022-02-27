import configparser
import datetime

import os
import re

import xlrd


class ExcelData():
    # 初始化方法
    def __init__(self):
        # 定义一个属性接收文件路径
        cf = configparser.ConfigParser()
        cur_path = os.path.dirname(os.path.realpath(__file__))
        cf.read(cur_path + "\Pyconfig.config")
        excelDir = cf.get("IEDownload", "path")
        self.data_path = self.getExcelFile(excelDir)
        if not self.data_path:
            return
        # 使用xlrd模块打开excel表读取数据
        self.workbook = xlrd.open_workbook(self.data_path)
        # 根据工作表的名称获取工作表中的内容（方式①）
        # self.sheet = self.data.sheet_by_name(self.sheetname)
        # 根据工作表的索引获取工作表的内容（方式②）
        self.sheet = self.workbook.sheet_by_index(0)

        # 获取工作表的有效行数
        self.rowNum = self.sheet.nrows
        # 获取工作表的有效列数
        self.colNum = self.sheet.ncols

        # 表头都需要分析出来
        if self.colNum:
            self.keys = self.getKeys()

        self.dbcol = {'交易日期': 'TRANS_DATE',
                         '借方发生额': '借方发生额',
                         '贷方发生额': 'LENDER_AMOUNT',
                         '余额': 'BALANCE',
                         '对方账号': 'OPPOSITE_ACCT',
                         '对方户名': 'OPPOSITE_NAME',
                         '凭证号': '凭证号',
                         '摘要':'摘要',
                         '用途': '用途',
                         '备注': '备注'
                     }

    def getKeys(self):
        sublist = ['交易日期', '借方发生额', '贷方发生额']

        for n in range(1, self.rowNum):
            keys = [val.strip() for val in self.sheet.row_values(n)]
            flag = [True for v in sublist if v not in keys]
            if not flag:
                break
        return keys

    def getData(self):
        rows = []
        for n in range(1, self.rowNum):
            values = self.sheet.row_values(n)
            if values.count('') <= 4:
                rows.append(values)

            if values.count('') == 8 and "账户:" in values:
                person_acct = values[1]
        return rows[1:], person_acct

    # 定义一个读取excel表的方法
    def readExcel(self):
        # 定义一个空列表
        rows, person_acct = self.getData()
        datas = []
        # 返回从excel中获取到的数据：以列表存字典的形式返回
        for rowData in rows:
            # 定义一个空字典
            sheet_data = {}
            for j in range(self.colNum):
                sheet_data[self.dbcol[self.keys[j]]] = rowData[j]
            sheet_data['PERSON_ACCT'] = person_acct
            datas.append(sheet_data)
        return datas

    def getExcelFile(self, excelDir):
        excels = []
        files = os.listdir(excelDir)
        for fi in files:
            regx = "^当日账户交易明细查询\d+(.xls|.xlsx)$"
            match = re.search(regx, fi)
            if match:
                excels.append(os.path.join(excelDir, fi))
        print(excels)
        excels.sort(key=lambda f: os.path.getctime(f))
        print(excels[-1])
        today_excel = excels[-1]
        # 清理历史excel
        if len(excels) > 10:
            for i in range(0,len(excels)-1):
                os.remove(excels[i])
        fileName = os.path.split(today_excel)[1]
        date = re.findall(r'\d+', fileName)[0][0:8]
        today = datetime.date.today().strftime('%Y%m%d')
        # 判断是否为当日excel文件
        if not date == today:
            print('today no data.')
            return None

        return excels[-1]


if __name__ == "__main__":
    excel = ExcelData()
    if not excel.colNum:
        print("not data.")

