import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import mysql.connector
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')
detail = pd.read_sql_table('meal_order_detail1',con = engine)
detailGroup = detail[['order_id','counts','amounts']].groupby(by = 'order_id')

#apply方法的基本用法
print('订单详情表的菜品销量与售价的均值为: \n',detail[['counts','amounts']].apply(np.mean))

#使用apply方法进行聚合操作

#使用apply相比agg会多输出order_id一列，可能表示的是内存地址
print('订单详情表分组后前3组每组的均值为: \n',detailGroup.apply(np.mean).head(3))

print('订单详情表分组后前3组每组的标准差为: \n',detailGroup.apply(np.std).head(3))

#使用transform方法聚合数据
#使用transform方法将销量和售价翻倍
print('订单详情表的菜品销量和售价的两倍为: \n',detail[['counts','amounts']].transform(lambda x:x*2).head(4))

#使用transform实现  组内  离差标准化
#只能对组内实现离差标准化
#print('订单详情表分组后实现组内离差标准化后前5行为: \n',detailGroup[['counts','amounts']].
#transform(lambda x:(x.mean() - x.min())/(x.max()-x.min())).head())   #分母为0的数在python中显示为NaN,遇到无效值出现警告

#按照时间对菜品订单详情表进行拆分

#订单详情表按日期进行分组
#将字符串表示的时间转换为具有时间属性的数据类型，之后使用i.date()函数，把具体的时间去掉，只留下日期
detail['place_order_time'] = pd.to_datetime(detail['place_order_time'])

#i.date() 函数仅提取出来日期
detail['date'] = [i.date() for i in detail['place_order_time']]

detailGroup = detail[['date','counts','amounts']].groupby( by = 'date') #按照日期进行分组
print(detailGroup.size().head())

#使用agg计算单日菜品销售的平均单价和售价中位数

#求分组后的订单详情表每日菜品销售的平均单价和售价中位数
dayMean = detailGroup.agg({'amounts':np.mean})
print('订单详情表前5组单日菜品销售均价为；\n',dayMean.head())

dayMedian = detailGroup.agg({'amounts':np.median})
print('订单详情表前5组单日菜品售价中位数位: \n',dayMedian.head())

#使用apply方法统计单日菜品销售数目

#求取订单详情表中单日菜品的总销量
daySaleSum = detailGroup.apply(np.sum)['counts'] #单独取出counts这一列
print('订单详情表前5组单日菜品销售数目为 :\n',daySaleSum.head())