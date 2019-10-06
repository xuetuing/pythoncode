# -*- coding: utf-8 -*-
from matplotlib import pylab
import numpy as np
from datetime import datatime
import pandas as pd
import DataAPI  #数据API
import seaborn as sns  #美化matplotlib图表
sns.set_style('white')

# 获取数据示例
secID = '510050.XSHG'
start = '20160101'
end = '20181101'

security = DataAPI.MktFundGet(
    secID=secID, beginDate=start, endDate=end, field=['tradeDate', closePrice])
security['tradeDate'] = pd.to_datatime(security['tradeDate'])
security = security.set_index('tradeDate')
security.info()

security.tail()  #todo

#画图表
security[closePrice].plot(grid=False, figsize=(12,8))
sns.despine()

window_short = 20 #短期均线
window_long = 120 #长期均线
SD = 5%  #偏离度阈值

#均值计算，numpy的移动平均函数：rolling_mean
security['short_window'] = np.round(pd.rolling_mean(security['closePrice'], window=window_short), 2)
security['long_window'] = np.round(pd.rolling_mean(security['closePrice'], window=window_long), 2)
security[['closePrice', 'short_window', 'long_window'].tail()]

#将三条线画在一张图上
security[['closePrice', 'short_window', 'long_window']].plot(grid=False, figsize=(12, 8))
sns.despine()

#买入信号：短期均线高于 长期日均线，并且超过SD个点位
#卖出信号：不满足买入信号的所有情况
#'s-l'：短期-长期
security['s-l'] = security['short_window'] - security['long_window']
security['s-l'].tail()
#判断条件 s-l > SDxlong_window,支持买入, 定义Regime为True
#其他情形，卖出信号，定义Regime为False
security['Regime'] = np.where(security['s-l'] > security['long_window']*SD, 1, 0)
security['Regime'].value_counts()  #统计了买入/卖出信号次数

#信号时间分布
security['Regime'].plot(grid=False, lw=1.5, figsize=(12, 8))
pylab.ylim((-0.1, 1.1))
sns.despine()

#在有了信号之后执行买入/卖出操作，再计算每日收益
security['Market'] = np.log(security['closePrice'] / security['closePrice'].shift(1))
security['Strategy'] = security['Regime'].shift(1) * security['Market']
security[['Market', 'Strategy', 'Regime']].tail()

#累计收益率
security[['Market', 'Strategy']].cumsum().apply(np.exp).plot(grid=False, figsize=(12, 8))
sns.despine()


