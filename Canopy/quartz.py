#使用quartz框架实现策略

start = datetime(2008, 1, 1)				# 回测起始时间
end  = datetime(2015, 4, 23)				# 回测结束时间
benchmark = 'SH50'							# 策略参考标准
universe = ['510050.XSHG']	# 股票池
capital_base = 100000     # 起始资金
commission = Commission(0.0,0.0)

window_short = 20
window_long = 120
longest_history = window_long
SD = 0.05

def initialize(account):					# 初始化虚拟账户状态
    account.fund = universe[0]
    account.SD = SD
    account.window_short = window_short
    account.window_long = window_long

def handle_data(account):             # 每个交易日的买入卖出指令
    hist = account.get_history(longest_history)
    fund = account.fund
    short_mean = np.mean(hist[fund]['closePrice'][-account.window_short:]) # 计算短均线值
    long_mean = np.mean(hist[fund]['closePrice'][-account.window_long:])   #计算长均线值
    
    # 计算买入卖出信号
    flag = True if (short_mean - long_mean) > account.SD * long_mean else False 
    if flag:
        if account.position.secpos.get(fund, 0) == 0:
            # 空仓时全仓买入，买入股数为100的整数倍
            approximationAmount = int(account.cash / hist[fund]['closePrice'][-1]/100.0) * 100
            order(fund, approximationAmount)
    else:
        # 卖出时，全仓清空
        if account.position.secpos.get(fund, 0) >= 0:
            order_to(fund, 0)