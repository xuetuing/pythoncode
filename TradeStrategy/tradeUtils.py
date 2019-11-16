class TradeUtils(object):
    # d周期内的最低值的值，x 为最低值 
    def llv(self, lowPriceList, period):
        return min(lowPriceList)
       
    def hhv(self, type, highPriceList):
        tp = type.upper()
        if tp == "H" or tp == "HIGH":
            return max(highPriceList)
        return None
    '''
    n天前的某种值,param(H,V,C...funtion)
    param可以传需要的值类型，或者一个函数，通过paramType(data,func)来指定
    '''
    def ref(self, param, n, *, paramType):
        return None

    def refDate(self, param, n, *, paramType):
        return None

    def rsv(self,closeList):
        pass