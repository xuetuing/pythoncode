# 选股,此部分由通达信手动触发选择
from quantstrategy.DealFile import *


def pickstock():
    # 每天开盘前加载前一天选出的股票
    now = datetime.date.today() - datetime.timedelta(days=3)
    stockdir = 'D:\Test'
    stockfiles = walkfile(stockdir)
    stockfile = selectfile(stockfiles, now.strftime('%Y-%m-%d'))
    stocks = getstocks(stockfile)
    print(stocks)


if __name__ == '__main__':
    '''test'''
    pickstock()