# 选股,此部分由通达信手动触发选择
from quantstrategy.DealFile import *


def pick_stock():
    # 每天开盘前加载前一天选出的股票
    now = datetime.date.today() - datetime.timedelta(days=3)
    stockdir = 'D:\Test'
    stocks = getstocks(stockdir, now.strftime('%Y-%m-%d'))
    print(stocks)


if __name__ == '__main__':
    '''test'''
    pickstock()