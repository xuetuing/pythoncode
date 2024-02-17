# 通达信分钟级数据处理，lc1,lc5文件处理，数据入库
from pytdx.reader import TdxLCMinBarReader, TdxFileNotFoundException
import pymysql
from datetime import datetime
import os.path
from DealFile import walkfile


def save_all_data(dataDir):
    stock_files = walkfile(dataDir)
    for file in stock_files:
        print(file)
        save_stock_info(file)

def save_stock_info(path):
    ''' 
    Desc: 读取lc5文件内容
    '''
    # path = '/home/mi/Downloads/c5/sz000001.lc5'
    basename = os.path.basename(path)
    name = os.path.splitext(basename)[0]
    code = name[2:]

    reader = TdxLCMinBarReader()
    df = reader.get_df(path)
    # print(df)
    dataMap = {}
    for index, row in df.iterrows():
        date_obj = index.to_pydatetime()
        year = date_obj.year
        # print(year)
        if dataMap.get(year) is None:
            dataMap[year] = []

        dataList = dataMap[year]
        data = {}
        data['code'] = code
        data['trade_date'] = index
        data['open'] = row['open']
        data['high'] = row['high']
        data['low'] = row['low']
        data['close'] = row['close']
        data['amount'] = row['amount']
        data['vol'] = row['volume']
        dataList.append(data)

    # print(dataList)
    print(dataMap.keys())
    
    # 批量插入数据库
    for key, val in dataMap.items():
        insert(key, val)

def insert(year, datas):
    con = get_connect()
    try:
        with con.cursor() as cursor:
            values =  list(map(lambda x: tuple(x.values()), datas))
            # values.append(('000001', datetime.strptime('2020-09-01 10:20:00', '%Y-%m-%d %H:%M:%S'), '11.01', '12.01', '11.00', '11.59', '15644664.0', '166464652'))

            sql = "insert into stock_info_{}(code, trade_date, open, high, low, close, amount, vol) values(%s, %s, %s, %s, %s, %s, %s, %s)".format(year)
            print(sql)
            cursor.executemany(sql, values)
            con.commit()
            cursor.close()
            # datas = cursor.fetchall()
            # print("获取的数据:\n", datas)
    except Exception as e:
        print("插入数据异常.\n", e)
    finally:
        con.close()


def query_by_range(code, startTime, endTime):
    con = get_connect()
    try:
        with con.cursor() as cursor:
            sql = "select * from stock_info where code = '{}' and trade_date >= '{}' and trade_date <= '{}'".format(code, startTime, endTime)
            print(sql)
            cursor.execute(sql)
            datas = cursor.fetchall()
            print("获取的数据:\n", datas)
    except Exception as e:
        print("插入数据异常.\n", e)
    finally:
        con.close()


def query(code, time):
    con = get_connect()
    try:
        with con.cursor() as cursor:
            sql = "select * from stock_info where code = '{}' and trade_date = '{}'".format(code, time)
            print(sql)
            cursor.execute(sql)
            datas = cursor.fetchone()
            print("获取的数据:\n", datas)
    except Exception as e:
        print("插入数据异常.\n", e)
    finally:
        con.close()


def get_connect():
    return pymysql.connect(
            host='127.0.0.1',
            port=3306,
            database='stock',
            charset='utf8',
            user='root',
            password='root'
        )


if __name__ == '__main__':
    # save_stock_info('')
    ''' 测试
    '''
    save_all_data('/home/mi/Downloads/c5')