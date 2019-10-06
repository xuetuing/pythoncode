#过滤规则：EMA快线上穿慢线
import talib
import datetime

security= ["000725.XSHE"]
today = datetime.date.today()
for i in security:
    df = get_price(i,end_date=today, frequency='daily', 
        fields=None, skip_paused=True, fq='pre', count=10, panel=True)
    #print(df)
    close = [float(x) for x in df['close']]
    df['EMA10'] = talib.EMA(np.array(close), timeperiod=10)
    df['EMA100'] = talib.EMA(np.array(close), timeperiod=100)
    #得到当前EMA值
    EMA10 = df['EMA10'][-1]
    EMA100 = df['EMA100'][-1]
    #前一天
    refEMA10 = df['EMA10'][-2]
    refEMA100 = df['EMA100'][-2]
    if(refEMA10 < refEMA100 && EMA10 > EMA100)：
        selectFlag = true
    
    
	df['MACD'],df['MACDsignal'],df['MACDhist'] = talib.MACD(np.array(close),fastperiod=12, slowperiod=24, signalperiod=18)   
	#print(i)
    
    
    
