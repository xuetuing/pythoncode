# 预先过滤，主要完成停牌，st, 不符合价格...股票的过滤
class PreFilters:
    # 是否停牌
    def suspendStatu(self, lag, stocksInfo):
        unsuspend_index = stocksInfo.iloc[:,0]<1
        unsuspend_stock_ = list(stocksInfo[unsuspend_index].index)
        # 进一步筛选出最近lag+1日未曾停牌的股票list
        unsuspend_stock = []
        for stock in unsuspend_stock_:
            if sum(attribute_history(stock,lag+1,'1d',('paused'),skip_paused=False))[0]==0:
                unsuspend_stock.append(stock)
        # 如果没有符合要求的股票则返回空
        if unsuspend_stock == []:
            log.info('没有过去十日没停牌的股票')
        return unsuspend_stock

    # 是否为ST股票
    def isST(self, stocksInfo):
        return stocksInfo

    # 价格是否小于32
    def checkPrice(self, stocksInfo):
        return stocksInfo