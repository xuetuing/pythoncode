import talib as tb
# 根据选股指标过滤
class SelectStocksFilters(object):
    # EMPA指标快线上穿慢线
    def checkEMPA(self,stock):
        pass
    
    # 每股价格 < 32
    def checkPrice(self):
        pass

    # 庄家筹码 > 85%
    def chipOfDealer(self):
        N = 34
        df = get_price(i,end_date=today, frequency='daily', fields=None, skip_paused=True, fq='pre', count=1, panel=True)
        print(df)
        
        close = df.iloc[0]["close"]
        rsv = (close-llv("low",N))/(hhv("high",N)-llv("low",N))*100
        
        K = tb.SMA(rsv,3,1)
        D = tb.SMA(K,3,1)
        J = 3*K-2*D
        return tb.EMA(J, 6)