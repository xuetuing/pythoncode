#加载库函数
import datetime                       #加载时间函数库
#初始化回测环境
start = '20170101'                    # 回测起始时间 注：支持两种日期表述形式（ '2015-01-01'，'20150101'）
end = '20181001'                      # 回测结束时间
benchmark = '000002.ZICN'             # 策略参考标准为A股指数
universe = set_universe('A')          # 证券池：可供选择的股票的范围为A股.（由于选股条件比较苛刻，所以为了保证有充足的可供选择股票，因此以整个A股作为投资范围）
freq = 'd'                            # 用日线回测的策略
refresh_rate = 10                     # 每10日调一次仓，即每个交易日都会运行第三部分的handle_data函数

#初始化投资者（账户）参数
#accounts为字典类型，代表投资者所有的账户，而字典中每一个键代表一个账户，而每一个键对应的值为该账户的初始情况，如本程序中的键为fantasy_account（股票账户），值为相应配置
accounts = {
    'fantasy_account': AccountConfig(account_type='security', capital_base=10000000)  #初始化投资者的股票账户： 投资品种为股票，初始投资金额为1千万
}

#初始化策略参数:
Max_Position = 1000000                #每只股票的买入限额为1,000，000元

#初始化回测环境，指明创建账户时的工作，全局只运行一次
def initialize(context):
    pass
        
#handle_data函数是策略的核心函数，包含了所有策略算法的内容，包括数据获取，交易信号生成，订单委托等逻辑。
#handle_data函数无论是回测还是模拟交易场景，这个函数会根据回测频率 freq 的设置被调用。当freq='d'时，每天被调用一次，当freq='m'时，每分钟被调用一次。
def handle_data(context):
    buylist = stock_sellection_Graham_positove_stock(context)  # 基于本杰明•格雷厄姆积极选股思想的选股策略
    trading(buylist,context)                                   # 基于固定投资额的仓位管理策略

def stock_sellection_Graham_positove_stock(context):
   
    """
    操盘规则(预测）: 
    * 股票市盈率高于市场平均水平
    * 股票的市净率低于3
    * 企业的流动比率大于1.1
    * 企业的长期负债与营运资金(流动资产-流动负债)比率不超过5
    * 净利润增长率处于较高水平
    """
    
    #数据获取（通用部分）：投资者账户，可供投资股票  
    previous_date = context.previous_date                                                           #获取上一交易日的时间
    previous_date = previous_date.strftime('%Y%m%d')                                                #将日期格式调整为%Y%m%d形式（20150227），方便读取因子数据
    account = context.get_account('fantasy_account')                                                #获取投资者的股票账户（fantasy_account）
    current_universe = context.get_universe(asset_type = 'stock',exclude_halt=True)                 #获取当前除停牌外的所有可供投资股票（universe）                                         
    #数据获取（策略需要数据）: 市盈率数据（PE），市净率（PB），流动比率（CurrentRatio），长期资本（LongDebtToWorkingCapital），净利润增长率（NetProfitGrowRate）                              
    data = DataAPI.MktStockFactorsOneDayGet(tradeDate=previous_date,secID=universe,ticker=u""
                                ,field=u"secID,tradeDate,PE,PB,CurrentRatio,LongDebtToWorkingCapital,NetProfitGrowRate",pandas="1")  
       
    #数据处理部分（数据结构部分）： 设定索引
    data = data.dropna()                                                                            #去掉无效数据
    #数据处理部分（策略计算部分）：
  #  data['PE'] = 1.0 / data['PE']                                                                   # PE转化为EP
    #策略构建部分：选择积极股（股票市盈率低于市场平均水平，股票的市净率低于3，企业的流动比率大于1.1，企业的长期负债与营运资金(流动资产-流动负债)比率不超过5，净利润增长率处于较高水平）生成buylist
    data = data[(data.PB < 3) & (data.PB > 0) & (data.PE > data.PE.quantile(0.8)) & (data.CurrentRatio > 1.1) & (data.LongDebtToWorkingCapital < 5)  &(data.NetProfitGrowRate >data.NetProfitGrowRate.quantile(0.8))]                                       #通过指标选择，生成股票集合（quantile(0.8)为80%分位数）
    buylist =  data['secID'].tolist()                                                                 #选择积极股,生成buylist
    return  list(buylist)                                                                             #返回buylist

def trading(buylist,context):   
    #仓位管理：单只股票的买入限额为1000，000元

    
    #数据获取（通用部分）：投资者账户，可供投资股票
    account = context.get_account('fantasy_account')                                        #获取投资者的股票账户（fantasy_account）
    current_universe = context.get_universe(asset_type = 'stock',exclude_halt=True)         #获取当前除停牌外的所有可供投资股票（universe）   
    security_position = account.get_positions()                                             #字典型数据，上一K线结束后的有效证券头寸，即持仓数量大于0的证券及其头寸
    cash = account.cash                                                                     #获取股票账户可用于投资的现金额度

    #交易执行部分：卖出
    for sec in current_universe:
        if sec not in buylist and sec in security_position:                             #不在buylist中，且有持仓，卖出        
            account.order_to(sec,0)                                                     #执行卖出指令
            cash += security_position[sec].amount * context.current_price(sec)          #估计卖出股票后的账户金额，注：context.current_price(sec) 是获取sec股票当前价格
    #交易执行部分：买入
    d = min(len(buylist), int(cash) // Max_Position)                                    #可以买入的股票数量，如果资金不够，只买入部分
    for sec in buylist[:d]:                                                             #买入buylist中前d只股票，d<=len(buylist)
        if sec not in security_position:
            account.order(sec, Max_Position / context.current_price(sec))                           #基于仓位管理的需要，每只股票最大投资额为100000元        