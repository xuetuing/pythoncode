# coding: utf-8

##### 下方代码为 IDE 运行必备代码 ##### 
if __name__ == '__main__':
    import jqsdk
    params = {
        'token':'f619bf362d7f969e58b2c5fad0bca29d', # 在客户端系统设置中找，字符串格式，例如 'asdf...'
        'algorithmId':1, # 在客户端我的策略中，整数型，例如：1；回测结束后在客户端此ID策略的回测列表中找对应的回测结果
        'baseCapital':1000000,
        'frequency':'day',
        'startTime':'2017-06-01',
        'endTime':'2017-08-01',
        'name':"Test1",
    }
    jqsdk.run(params)

##### 下面是策略代码编辑部分 #####

import jqdata

def initialize(context):
    set_benchmark('000300.XSHG')
    set_option('use_real_price', True)
    log.info('initialize run only once')
    run_daily(market_open, time='open', reference_security='000300.XSHG')

def market_open(context):
    # 输出开盘时间
    log.info('(market_open):' + str(context.current_dt.time()))