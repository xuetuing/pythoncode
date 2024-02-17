# 工具类


from chinese_calendar import is_workday
from datetime import datetime

def is_trading_day(date):
    if is_workday(date):
      if datetime.isoweekday(date) < 6:
         return True
    return False


if __name__ == '__main__':
    date = '2023-12-31'
    date = datetime.strptime(date, '%Y-%m-%d').date()
    print(is_trading_day(date))