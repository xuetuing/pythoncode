class TradeUtils(object):
    # d周期内的最低值的值，x 为最低值 
    def llv(self, type, lowPriceList):
        tp = type.upper()
        if tp == "L" or tp == "LOW":
            return max(lowPriceList)
        return None
    def hhv(self, type, highPriceList):
        tp = type.upper()
        if tp == "H" or tp == "HIGH":
            return max(highPriceList)
        return None