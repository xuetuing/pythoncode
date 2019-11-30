import numpy as np
from functools import reduce
import talib as ta
class TradeUtils(object):
    N = 34
    # d周期内的最低值的值，x 为最低值 
    def llv(self, stockInfo, period):
        closeList = stockInfo[:]['close'].values
        print(closeList)
        result = []
        for i in range(closeList.size-1,-1,-1):
            temList = closeList[i-period+1:i+1]
            if(temList.size < period):
                minPrice = None
            else:
                minPrice = min(temList)
            result.append(minPrice)
            print(minPrice)
        print(result)
        return result
       
    def hhv(self, stockInfo, period):
        closeList = stockInfo[:]['close'].values
        print(closeList)
        result = []
        for i in range(closeList.size-1,-1,-1):
            temList = closeList[i-period+1:i+1]
            if(temList.size < period):
                maxPrice = None
            else:
                maxPrice = min(temList)
            result.append(maxPrice)
            print(maxPrice)
        print(result)
        return result
    # RSV:=(CLOSE-LLV(LOW,N))/(HHV(HIGH,N)-LLV(LOW,N))*100; 
    def rsv(self, stockInfo):
        closeList = stockInfo[:]['close'].values
        llv_per = llv(stockInfo, N)
        hhv_per = hhv(stockInfo, N)
        result = []
        for i in range(closeList.size-1,-1,-1):
            if llv_per[i] == None or hhv_per[i] == None:
                rsv_value = None
            else:
                rsv_value = (closeList[i]-llv_per[i])/(hhv_per[i]-llv_per[i])*100
            result.append(rsv_value)
            print(rsv_value)
        print(result)
        return result
    # K:=SMA(RSV,3);
    def k(self, stockInfo, period):
        rsv_per = rsv(stockInfo)
        return ta.SMA(np.array(rsv_per), period)
        
    # D:=SMA(K,3);
    def d(self, stockInfo, period):
        k_per = k(stockInfo, period)
        return ta.SMA(k_per, period)
    # J:=3*K-2*D;
    def j(self, stockInfo, period):
        k_per = k(stockInfo, period)
        d_per = d(stockInfo, period)
        result = []
        for i in range(k_per.size-1,-1,-1):
            if k_per[i] == None or d_per[i] == None:
                j_value = None
            else:
                j_value = 3*k_per[i] - 2*d_per[i]
            result.append(j_value)
            print(j_value)
        print(result)
        return result

     '''
    n天前的某种值,param(H,V,C...funtion)
    param可以传需要的值类型，或者一个函数，通过paramType(data,func)来指定
    '''
    def ref(self, param, n, *, paramType):
        return None

    def refDate(self, param, n, *, paramType):
        return None
        