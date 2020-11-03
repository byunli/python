import requests
from datetime import datetime, date, timedelta

# today = date.today()
# print('今天的日期')
# # print(type(today))
# print(today)
# print('-'*30)

# 輸入日期
# 判斷日期是否在2020年11月
# date1 = input('請出入日期 格式如yyyy-mm-dd: ')
# date1_object = date.fromisoformat(date1)

# datetime_object1101 = date.fromisoformat('2020-11-01')
# datetime_object1130 = date.fromisoformat('2020-12-01')

# if date1_object<datetime_object1101 or date1_object>datetime_object1130:
#     print('不在11月')
# else:
#     print('在11月')

# # 判斷日期是否在下個月
# date1 = input('請出入日期 格式如yyyy-mm-dd: ')
# date1_object = date.fromisoformat(date1)

# datetime_object1201 = date.fromisoformat('2020-12-01')
# datetime_object1231 = date.fromisoformat('2021-01-01')

# if date1_object<datetime_object1201 or date1_object>datetime_object1231:
#     print('在下個月')
# else:
#     print('不在下個月')


# 輸入一個年月日(yyyy/mmm/dd)
# 日期轉變成字串
# str_today = str(today)
# date1 = input('請出入日期 格式如xxxx-xx-xx: ')
# date1 = datetime.strptime(date1,'%Y/%m/%d').date()

# ---------------------
# 取得今天日期
today = date.today()
print('今天的日期')
print(today)
print('-'*30)

# 取得今天的年份和月份
month = today.month
year = today.year

nextMonth = month + 1
nextYear = year + 1

if month == 12:
    nextMonth = 1
    nextYear += 1

print('next month = ',nextMonth)
print('nextYear = ',nextYear)

# try:
#   nextmonthdate = x.replace(month=x.month+1)
# except ValueError:
#   if x.month == 12:
#     nextmonthdate = x.replace(year=x.year+1, month=1)
#   else:
#     # next month is too short to have "same date"
#     # pick your own heuristic, or re-raise the exception:
#     raise

# 取得下個月
# import datetime
# from dateutil import relativedelta
# nextmonth = datetime.date.today() + relativedelta.relativedelta(months=1)
# print(nextmonth)



# tomorrow = today + timedelta(days=1)
# print('明天的日期')
# print(tomorrow)
# print('-'*30)

# strftime = datetime.datetime.strptime("2017-11-02", "%Y-%m-%d")
# strftime2 = datetime.datetime.strptime("2017-01-04", "%Y-%m-%d")
# print("2017-11-02大于2017-01-04：",strftime>strftime2)
