# 克隆自聚宽文章：https://www.joinquant.com/post/19856
# 标题：優化 EMA+Macd指標策略
# 作者：kkcmos

# 导入函数库
from kuanke.wizard import *
from jqdata import *
import numpy as np
import pandas as pd
import talib
import datetime

# 初始化函数，设定基准等等
def initialize(context):
   g.security=["000725.XSHE","000063.XSHE","601318.XSHG","000050.XSHE","600518.XSHG","601939.XSHG"]
   
   
## 开盘前运行函数     
def handle_data(context, data):
    
    for i in g.security:
       df = attribute_history(i,300,unit='1d',
            fields=['open', 'close', 'high', 'low', 'volume', 'money'],
            skip_paused=True, df=True, fq='pre') 
       #df = panel['open'] i
       close = [float(x) for x in df['close']]
       df['EMA10'] = talib.EMA(np.array(close), timeperiod=10)
       df['EMA100'] = talib.EMA(np.array(close), timeperiod=100)  
       df['MACD'],df['MACDsignal'],df['MACDhist'] = talib.MACD(np.array(close),fastperiod=12, slowperiod=24, signalperiod=18)   
       #print(i)
       #print(df)
       #print(df.iloc[:,3])
       #print(df['MACD'][-1])
       
       #print(i)
       average_price_100=data[i].mavg(100,'close')
       average_price_10=data[i].mavg(10,'close')
       #last_price=data[i].close
       #print('last_price_data=')
       #print(last_price)
       #print(data[i])
       
       #print('--------')
       #print('last_price_df=')
       #print(df['close'][-1])
       #print(df)
       
       
       cash=3*context.portfolio.cash/(len(g.security))
       
       cost=context.portfolio.positions[i].avg_cost
       price=context.portfolio.positions[i].price
       
       last_price=df['close'][-1]
       #average_price_100=df['EMA100'][-1]
       #average_price_10=df['EMA10'][-1]
       
       #print(i)
       #print('average_price_100_df')
       #print(df['EMA100'][-1])
       #print('---------')
       #print('average_price_100_da')
       #print(data[i].mavg(100,'close'))
       #print(average_price_10)
       #print(average_price_100)
       
       
       if cost==0:
          ret=0
       
       if cost!=0:
          ret=price/cost-1
       
       #if last_price>average_price_100 and average_price_10>average_price_100 :
       if last_price>average_price_100 and average_price_10>average_price_100 and  last_price>average_price_10 and df['MACDhist'][-1]>df['MACDhist'][-2]:
           send_message('BUY---')
           send_message(get_security_info(i))
           print(get_security_info(i))
           
           if i not in context.portfolio.positions:
               order_value(i,cash)
               #print('buy')
     
       elif last_price<average_price_100 or average_price_10<average_price_100 or ret<-0.11:
           if i in context.portfolio.positions:
              order_target(i,0)
       
       
