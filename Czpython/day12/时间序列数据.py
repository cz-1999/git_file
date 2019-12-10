from sqlalchemy import create_engine
import pandas as pd
#创建一个MYSQL连接器，用户名为root,密码为1234
#地址为127.0.0.1,数据库名称为testdb,编码为UTF-8
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')

#使用read_sql_table读取订单详情表
detail1 = pd.read_sql_table('meal_order_detail1',con = engine)

order = pd.read_csv('D:/python/czpython/meal_order_info.csv',encoding = 'gbk')
print('进行转换前订单信息表lock_time的数据类型为: ',order['lock_time'].dtypes)
print(order['lock_time'])

order['lock_time'] = pd.to_datetime(order['lock_time'])
print('进行转换后订单信息表lock_time的数据类型为: ',order['lock_time'].dtypes)
print(order['lock_time'])

print('最小时间为: ',pd.Timestamp.min)
print('最大时间为: ',pd.Timestamp.max)#哪的时间?????????

dateIndex = pd.DatetimeIndex(order['lock_time'])
print('转换为DatetimeIndex后数据的类型为',type(dateIndex))
print(order['lock_time'])

periodIndex = pd.PeriodIndex(order['lock_time'],freq = 'S')
print('转换为PeriodIndex后数据的类型为',type(dateIndex))
print(order['lock_time'])

#要将order['lock_time']字符串表示的时间转换为具有时间属性的时间数据类型
year1 = [i.year for i in order['lock_time']]
print('lock_time中的年份数据前5个为 : ',year1[:5])
month1 = [i.month for i in order['lock_time']]
print('lock_time中的月份数据前5个为 : ',month1[:5])
day1 = [i.day for i in order['lock_time']]
print('lock_time中的日期数据前5个为 : ',day1[:5])
weekday1 = [i.weekday_name for i in order['lock_time']]
print('lock_time中的星期名称数据前5个为 : ',weekday1[:5])

print('dateIndex中的星期名称数据前5个为: \n',dateIndex.weekday_name[:5])
print('periodIndex中的星期标号数据前5个为: \n',periodIndex.weekday[:5])#?????

#将lock_time数据向后平移一天
#pd.Timedelta() 可以前后平移时间的函数，可以平移days,和weeks
time1 = order['lock_time']+pd.Timedelta(days = 1 )
print('lock_time在加上一天前前5行数据为；',order['lock_time'][:5])
print('lock_time在加上一天后前5行数据为；',time1[:5])

#
timeDelta = order['lock_time'] - pd.to_datetime(2017-1-1) #????
print('lock_time减去2017年1月1日0时0分0秒后的数据；',timeDelta[:5])
print('lock_time减去time1后的数据类型为:',timeDelta.dtypes)



#任务实现
order['use_start_time'] = pd.to_datetime(order['use_start_time'])
order['lock_time'] = pd.to_datetime(order['lock_time'])
print('进行转换后订单信息表的user_start_time和lock_time的数据类型为: \n',order[['use_start_time','lock_time']].dtypes)

year = [i.year for i in order['lock_time']]#提取年份信息
month = [i.month for i in order['lock_time']]#提取月份信息
day = [i.day for i in order['lock_time']]#提取日期信息
week = [i.week for i in order['lock_time']]#提取周信息
weekday = [i.weekday for i in order['lock_time']]#提取星期信息
weekname = [i.weekday_name for i in order['lock_time']]#提取星期名称信息

print('订单详情表中的前5条数据的年份信息为: ',year[:5])
print('订单详情表中的前5条数据的月份信息为: ',year[:5])
print('订单详情表中的前5条数据的日期信息为: ',year[:5])
print('订单详情表中的前5条数据的周信息为: ',year[:5])
print('订单详情表中的前5条数据的星期信息为: ',year[:5])
print('订单详情表中的前5条数据的星期名称信息为: ',year[:5])


timemin = order['lock_time'].min()
timemax = order['lock_time'].max()
print('订单最早时间为；',timemin)
print('订单最晚时间为；',timemax)
print('订单持续时间为；',timemax-timemin)
print(order['use_start_time'])
checkTime = order['lock_time']- order['use_start_time']
print('平均点餐时间为: ',checkTime.mean())
print('最小点餐时间为: ',checkTime.min())###-1天 ????
print('最大点餐时间为: ',checkTime.max())
