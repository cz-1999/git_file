from sqlalchemy import create_engine
import pandas as pd
import numpy as np
#创建一个MYSQL连接器，用户名为root,密码为1234
#地址为127.0.0.1,数据库名称为testdb,编码为UTF-8
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')

#使用read_sql_table读取订单详情表
detail1 = pd.read_sql_table('meal_order_detail1',con = engine)
print('使用read_sql_table读取订单详情表的长度为：',len(detail1))#行数

#使用np.mean函数计算平均价格
print('订单详情表中amount(价格）的平均值为: ',np.mean(detail1['amounts']))

#通过pandas实现销量和价格的协方差矩阵计算
print('订单详情表中amount(价格）的平均值为:',detail1['amounts'].mean())

#使用describe方法实现数值型特征的描述性统计
print('订单详情表counts和amounts两列的描述性统计为: \n',detail1[['counts','amounts']].describe())

#对菜品名称频数进行统计，实现频数统计的函数value_counts,对菜品销售数据中的蔡明进行频数统计
print('订单详情表dishes_name频数统计结果前10为：\n',detail1['dishes_name'].value_counts()[0:10])

#pandas提供了category类,可以使用astype方法将目标特征数据类型转换为category类,可以使用astype方法将目标特征的数据类型
#转换为category类型

#将object数据强制转化成category类型
detail1['dishes_name'] = detail1['dishes_name'].astype('category')
print('订单详情表dishes_name列转变数据类型后为: ',detail1['dishes_name'].dtype)

#category类型特征描述性统计
#不进行强制类型转换也能实现 detail1['dishes_name'].describe()
#4个统计量分别为列非空元素的数目、类别的数目、数目最多的类别、和数目最多类别的数目
print('订单详情表dishes_name的描述统计结果为: \n',detail1['dishes_name'].describe())

