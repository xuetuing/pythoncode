# 克隆自聚宽文章：https://www.joinquant.com/post/8325
# 标题：量化“抓妖”新尝试——布林带“开口型喇叭口”股票投资策略
# 作者：wtj

# 导入函数库
import jqdata
# 导入pandas
import pandas
# 导入技术分析指标函数
from jqlib.technical_analysis import *
# 导入ta-lib
import talib
import PreFilters
from operator import methodcaller
# 初始化函数，设定基准等等
def initialize(context):
    # 设置参数
    set_params()
    # 设置回测条件
    set_backtest()
    
    ### 股票相关设定 ###
    # 股票类每笔交易时的手续费是：买入时佣金万分之三，卖出时佣金万分之三加千分之一印花税, 每笔交易佣金最低扣5块钱
    set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5), type='stock')
    
    ## 运行函数（reference_security为运行时间的参考标的；传入的标的只做种类区分，因此传入'000300.XSHG'或'510300.XSHG'是一样的）
      # 开盘前运行
    run_daily(before_market_open, time='before_open', reference_security='000300.XSHG') 
      # 收盘后运行
    run_daily(after_market_close, time='after_close', reference_security='000300.XSHG')

def set_params():
    # 设定沪深300作为基准
    set_benchmark('000300.XSHG')
    # 设定策略相关参数
    g.lag = 200   # 最近200日未停牌
    g.Max = 1     # 最大持仓
    g.N = 0       # 持仓股数
    g.stock_set = '000300.XSHG' # 用来挑选股票的股票池
    
def set_backtest():
    # 开启动态复权模式(真实价格)
    set_option('use_real_price', True)
    # 过滤掉order系列API产生的比error级别低的log
    log.set_level('order', 'error')
    
## 开盘前运行函数     
def before_market_open(context):
    log.info(str('交易日期:'+str(context.current_dt)))
    # 如果有持仓股票，取出持仓股票代码，作为快收盘时监测是否卖出的股票池
    g.check_list = context.portfolio.positions.keys()
    g.N = len(g.check_list)
    # 如果持仓没有满，得到今日可以购买的股票列表
    log.info('g.N='+str(g.N))
    if g.N<g.Max:
        # 首先得到布林带宽在lim以内的股票
        g.buy_list = get_buy_list(context,g.lag,g.stock_set)
        if g.buy_list != []:
            # 得到今日股票前lag日的布林线数据
            up_line,mid_line,dn_line,width = get_bollinger(context,g.buy_list,g.lag)
            # 选取昨日放量上涨且收盘价位于布林中线以上且布林带放大的股票，
            # 依据昨日量价涨幅的综合评分对这些股票进行排序，取前Max-N个
            g.buy_list = grade_filter(g.buy_list,g.lag,up_line,width,context)
    # 如果持仓已满，则今天不购买股票
    else:
        g.buy_list = []
        log.info('今日不需购买股票')
    
# 
def get_buy_list(context,lag,stk_set):
    # 得到当日是否停牌的dataframe，停牌为1，未停牌为0
    try:    # 若股票池为指数
        suspend_info = get_price(get_index_stocks(stk_set),start_date=context.current_dt,end_date=context.current_dt,frequency='daily',fields='paused')['paused'].T
    except: # 若股票池不为指数
        suspend_info = get_price(stk_set,start_date=context.current_dt,end_date=context.current_dt,frequency='daily',fields='paused')['paused'].T
    # 执行股票过滤规则
    # 1. 初步过滤股票
    preFilterNameList = list(filter(lambda m: not m.startwith("__") and not m.endwith("__") and callable(getattr(PreFilters, m)), dir(PreFilters))) 
    for filterName in preFilterNameList:
        suspend_info = methodcaller(filterName)(suspend_info)

    if len(unsuspend_stock) != 0:
        log.info('今日潜在满足要求的标的有：'+str(len(unsuspend_stock)))
    return unsuspend_stock
    
def get_bollinger(context,buy,lag):
    # 创建以股票代码为index的dataframe对象来存储布林带信息
    dic = dict.fromkeys(buy,[0]*(lag+1)) # 创建一个以股票代码为keys的字典
    up = pandas.DataFrame.from_dict(dic).T # 用字典构造dataframe
    mid = pandas.DataFrame.from_dict(dic).T
    dn = pandas.DataFrame.from_dict(dic).T
    wd = pandas.DataFrame.from_dict(dic).T
    for stock in buy:
        for j in range(lag+1):
            up_,mid_,dn_ = Bollinger_Bands(stock,check_date=context.previous_date-datetime.timedelta(days=j),timeperiod=20,nbdevup=2,nbdevdn=2)
            up.loc[stock,j] = up_[stock]
            mid.loc[stock,j] = mid_[stock]
            dn.loc[stock,j] = dn_[stock]
            wd.loc[stock,j] = (up[j][stock] - dn[j][stock])/mid[j][stock]
    return up,mid,dn,wd
    
def grade_filter(buy,lag,up_line,wd,context):
    # 选出连续开口的股票
    pass   
    
def get_rank(por):
    # 定义一个数组记录一开始的位置
    indexes = range(len(por))
    # 对每一列进行冒泡排序
    for col in range(len(por[0])):
        for row in range(len(por)):
            for nrow in range(row):
                if por[nrow][col]<por[row][col]:
                    indexes[nrow],indexes[row] = indexes[row],indexes[nrow]
                    for ecol in range(len(por[0])):
                        por[nrow][ecol],por[row][ecol] = por[row][ecol],por[nrow][ecol]
        for row in range(len(por)):
            por[row][col] = row
    # 再对indexes进行一次冒泡排序，使por恢复原顺序，每一行与buy中的股票代码相对应
    for row in range(len(por)):
        for nrow in range(row):
            if indexes[nrow]<indexes[row]:
                indexes[nrow],indexes[row] = indexes[row],indexes[nrow]
                for col in range(len(por[0])):
                    por[nrow][col],por[row][col] = por[row][col],por[nrow][col]
    return por
                    
def grade_rank(grades,buys):
    for row in range(len(grades)):
        for nrow in range(row):
            if grades[nrow]>grades[row]:
                grades[nrow],grades[row] = grades[row],grades[nrow]
                buys[nrow],buys[row] = buys[row],buys[nrow]
    return grades,buys
    

## 开盘时运行函数
def handle_data(context,data):
    # 每天开盘时
    if context.current_dt.hour==9 and context.current_dt.minute==30:
        if g.buy_list != []:
            for stock in g.buy_list:
                order_target_value(stock,context.portfolio.available_cash/(g.Max-g.N))
                g.N =g.N+1
    # 每天收盘时决定是否出售
    if context.current_dt.hour>=9 and context.current_dt.minute>30:
        if g.check_list != []:
            # 得到持仓股昨日的收盘价
            pre_close = history(1,'1d','close',g.check_list)
            # 得到持仓股昨日的布林线信息
            up_info,mid_info,dn_info,wth_info = get_bollinger(context,g.check_list,0)
            # 得到前一分钟价格
            pre_min_price = history(1,'1m','close',g.check_list)
            current_data = get_current_data()
            for stock in g.check_list:
                i = 0
                '''
                # 若当日股票下跌5%，卖出股票
                if pre_min_price[stock][-1]<0.95*pre_close[stock][-1]:
                    order_target_value(stock,0)
                '''
                if context.current_dt.hour==14 and context.current_dt.minute==53:
                    # 若收盘价格接近触碰中线，卖出股票
                    if pre_min_price[stock][-1]<=1.01*mid_info.iloc[0,-1]:
                        order_target_value(stock,0)
                    
    
 
## 收盘后运行函数  
def after_market_close(context):
    #得到当天所有成交记录
    trades = get_trades()
    for _trade in trades.values():
        log.info('成交记录：'+str(_trade))
    log.info('##############################################################')
