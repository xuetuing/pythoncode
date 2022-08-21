import pandas as pd  
import numpy as np
#定时进行分时选择，选择出符合形态的股票进行买入
print('分时选股')

# 实时价格为下一分钟bar的收盘价
# h = attribute_history('002053.XSHE', 100, '1m', ('volume', 'money'))
# idx = h.index #获取索引中的时间
# for i in h.index:
#     print(type(i))
#     print(h.loc[i])

def pick_stock_by_min(stockList):
    """根据分时均线选出符合条件并排序后的stockList
    Args:
        stockList (List): 传入前日选出的股票列表
    Returns:
        [List]: 返回符合条件排序后的骨片列表
    """
    stockMapTmp = []
    for stock in stockList:
        # 分时均价线计算：1min数据，∑(money)/∑(vol)
        h = attribute_history(stock, 240, '1m', ('close', 'volume', 'money'))
        #h['newcol'] = h.apply(lambda col: col['money']/col['volume'], axis=1)

        #计算出k个时间点的均值 加入每小时取12个点，则每5分钟计算一次
        h['cumsum_money'] = h['money'].cumsum()
        h['cumsum_volume'] = h['volume'].cumsum()
        h['avg'] = h.apply(lambda col: round(col['cumsum_money']/col['cumsum_volume'], 2), axis=1)
        # 每5分钟取一次对比，记录对比结果
        compareRes = []
        cout = 0
        for index, row in h.iterrows():
            cout += 1;
            if cout % 5 == 0: 
                compareRes.append(row['close'] >= row['avg'])
        print((stock + " 'True' count:{}，Total:{}").format(compareRes.count(True), len(compareRes)))
        if compareRes.count(True) < len(compareRes) * 0.5:
            continue
        stockTemp = {}
        stockTemp['stockName'] = stock
        stockTemp['count'] = compareRes.count(True)
        stockMapTmp.append(stockTemp)
    #按True个数排序
    stockMapTmp.sort(key=lambda x: x['count'], reverse=True)
    print('stockMapTmp:'.format(stockMapTmp))
    selectedStocks = [x['stockName'] for x in stockMapTmp]
    print('selectedStocks:'.format(selectedStocks))
    return selectedStocks

