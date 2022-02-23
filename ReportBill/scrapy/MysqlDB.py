import configparser
import os
import pymysql

from scrapy.ExcelData import ExcelData


class MysqlDB():

    def __init__(self):
        cf = configparser.ConfigParser()
        cur_path = os.path.dirname(os.path.realpath(__file__))
        cf.read(cur_path + "\Pyconfig.config")
        _db = cf.get("Mysql", "database")
        _host = cf.get("Mysql", "host")
        _user = cf.get("Mysql", "user")
        _pwd = cf.get("Mysql", "passwd")
        self.conn = pymysql.connect(host=_host, port=3306, user=_user, passwd=_pwd, db=_db, charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()

    def selectData(self):
        count = self.cursor.execute("SELECT * FROM TRANSACTION")
        # self.cursor.execute("SELECT COUNT(*) FROM TRANSACTION T where T.TRANS_DATE=%s and T.PERSON_ACCT=%s" % ())
        return count

    def insertData(self, datas):
        count = self.selectData()
        datalen = len(datas)
        if count < datalen:
            for data in datas[count:]:
                self.cursor.execute('''insert into TRANSACTION(TRANS_DATE, PERSON_ACCT, LENDER_AMOUNT, BALANCE, OPPOSITE_ACCT,OPPOSITE_NAME,CREATED_TIME) 
                VALUES ('%s',%s,%s,%s,%s,'%s','%s')''' %(data['TRANS_DATE'],data['PERSON_ACCT'],data['LENDER_AMOUNT'],data['BALANCE'],data['OPPOSITE_ACCT'],data['OPPOSITE_NAME'],"2022-02-21"))
        self.conn.commit()


if __name__ == '__main__':
    '''
    db = MysqlDB()
    data_path = "C:\\Users\DELL\Downloads\当日账户交易明细查询20220220203935.xls"
    get_data = ExcelData(data_path)
    datas = get_data.readExcel()
    db.insertData(datas)
    print(datas)
    '''

