import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import mysql.connector
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')
detail = pd.read_sql_table('meal_order_detail1',con = engine)

#使用订单号作为透视表索引制作透视表
#当不特殊指定聚合函数aggfunc时，会默认使用np.mean进行聚合计算,np.mean会自动过滤掉非数值类型数据
#可以通过指aggfunc定参数来修改聚合函数

detailPivot = pd.pivot_table(detail[['order_id','counts','amounts']],index = 'order_id')
print('以order_id作为分组键创建的订单透视表为: \n',detailPivot.head())


#修改聚合函数后的透视表为
detailPivot = pd.pivot_table(detail[['order_id','counts','amounts']],index = 'order_id',aggfunc = np.sum)
print('以order_id作为分组键创建的订单销量与售价总和透视表为：\n',detailPivot.head())

#pivot_table函数和groupby分组方法相同,pivot_table函数在创建透视表时，分组键index可以有多个

#使用订单号和菜品名称作为索引的透视表
#透视表内容顺序 与分组键的顺序有关 ，与detail[[]]中的顺序无关
detailPivot2 = pd.pivot_table(detail[['dishes_name','order_id','counts','amounts']],index = ['order_id','dishes_name','order_id'],aggfunc = np.sum)
print('以order_id和dishes_name作为分组键创建的订单销量与售价总和透视表为：\n',detailPivot2.head())

#指定菜品名称为列分组键的透视表
detailPivot3 = pd.pivot_table(detail[['order_id','dishes_name','counts','amounts']],index = 'order_id',columns = 'dishes_name',
aggfunc = np.sum)
print('以order_id和dishes_name作为行列分组键创建的透视表前5行4列为: \n',detailPivot3.iloc[:5,:4])

#指定某些列制作透视表
detailPivot4 = pd.pivot_table(detail[['order_id','dishes_name','counts','amounts']],index = 'order_id',values = 'counts',
aggfunc = np.sum)

print('以order_id作为行分组键counts作为值创建的透视表前5行为: \n',detailPivot4.head())

#当某些数据不存在时，会自动填充NaN因此可以指定fill_value参数,表示当存在缺失值时以指定参数进行填充

#对透视表中缺失值进行填充
detailPivot5 = pd.pivot_table(detail[['order_id','dishes_name','counts','amounts']],index = 'order_id',columns = 'dishes_name',
aggfunc = np.sum,fill_value = 0)
print('空填值为0后，以order_id和dishes_name作为行列分组键创建的透视表前5行4列为: \n',detailPivot5.iloc[:5,:4])


#在透视表中添加新的汇总数据,All列对这一行所有的销量进行汇总
detailPivot6 = pd.pivot_table(detail[['order_id','dishes_name','counts','amounts']],index = 'order_id',columns = 'dishes_name',
aggfunc = np.sum,fill_value = 0,margins = True)
print('添加margins后以order_id和dishes_name作为行列分组键创建的透视表前5行后4列为: \n',detailPivot6.iloc[:5,-4:])

#使用crosstab函数创建交叉表
#交叉表是一种特殊的透视表，主要用于计算分组频率

detailCross = pd.crosstab(index = detail['order_id'],columns = detail['dishes_name'],values = detail['counts'],
                          aggfunc = np.sum )
print('以order_id和dishes_name为分组键counts为值的透视表前5行5列为: \n',detailCross.iloc[:5,:5])

#创建单日菜品成交总额与总数均价透视表

detail['place_order_time'] = pd.to_datetime(detail['place_order_time'])
detail['date'] = [i.date() for i in detail['place_order_time']]
PivotDetail = pd.pivot_table(detail[['date','dishes_name','counts','amounts']],index ='date',aggfunc=np.sum,margins=True)
print('订单详情表单日菜品成交总额与总数透视表前5行为: \n',PivotDetail.head())

#创建单个菜品单日成交总额透视表

#订单详情表单个菜品单日成交总额透视表
CrossDetail = pd.crosstab(index = detail['date'],columns=detail['dishes_name'],values = detail['amounts'],aggfunc=np.sum)
print('订单详情表单个菜品单日成交总额交叉表后5行5列为: \n',CrossDetail.iloc[-5:,-5:])