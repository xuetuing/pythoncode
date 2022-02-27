import configparser
import datetime
import os
import pymysql


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

    def selectData(self, person_acct):
        today = datetime.date.today()
        count = self.cursor.execute('''SELECT * 
          FROM TRANSACTION T WHERE T.TRANS_DATE='%s' AND T.PERSON_ACCT=%s''' % (today, person_acct))
        print("count: {}".format(count))
        return count

    def insertData(self, datas):
        today = datetime.date.today()
        print("person_acct: {}".format(datas[0]['PERSON_ACCT']))
        count = self.selectData(datas[0]['PERSON_ACCT'])
        datalen = len(datas)
        if count < datalen:
            for data in datas[count:]:
                self.cursor.execute('''insert into TRANSACTION(TRANS_DATE, PERSON_ACCT, LENDER_AMOUNT, BALANCE, OPPOSITE_ACCT,OPPOSITE_NAME,CREATED_TIME) 
                VALUES ('%s',%s,%s,%s,%s,'%s','%s')''' %(data['TRANS_DATE'],data['PERSON_ACCT'],data['LENDER_AMOUNT'],data['BALANCE'],data['OPPOSITE_ACCT'],data['OPPOSITE_NAME'],today))
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
    # print(datetime.date.today())

