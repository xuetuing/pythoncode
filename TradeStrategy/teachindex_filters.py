import talib as tb
from TradeUtils import j
# 根据选股指标过滤
class SelectStocksFilters(object):
    # EMPA指标快线上穿慢线
    def checkEMPA(self,stock):
        pass
    
    # 每股价格 < 32
    def checkPrice(self):
        pass

    # 庄家筹码 > 85%
    def chipOfDealer(self, stock):
        stockInfo = get_price(stock,end_date=today, frequency='daily', fields=None, skip_paused=True, fq='pre', count=80, panel=True)
        print(stockInfo)
        j_value = j(stockInfo, 3)
        return tb.EMA(J, 6)