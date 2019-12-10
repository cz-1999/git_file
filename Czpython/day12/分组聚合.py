import pandas as pd
import numpy as np
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')
detail = pd.read_sql_table('meal_order_detail1',con = engine)

#使用groupby方法拆分数据
#groupby方法提供的是分组聚合步骤中的拆分功能，能够根据
#agg函数对DataFrame进行操作输出一个总值，对Groupby分的组进行操作，输出每组的值


#通过order_id进行分组,order_id相同的为一组
detailGroup = detail[['order_id','counts','amounts']].groupby(by = 'order_id')
print('分组后的订单详情表为:',detailGroup)

print('订单详情表分组后前5组每组的均值为: \n',detailGroup.mean().head())
print('订单详情表分组后前5组每组的标准差为: \n',detailGroup.std().head())
print('订单详情表分组后前5组每组的大小为: \n',detailGroup.size().head())

#使用agg方法聚合数据

#使用agg求出当前数据对应的统计量
print('订单详情表的菜品销量与售价的和与均值为: \n',detail[['counts','amounts']].agg([np.sum,np.mean]))
#使用agg分别求字段的不同统计量
#此时需要使用字典的方式，将两个字段名分别作为key，然后将Numpy库的求和与求均值的函数分别作为values
print('订单详情表的菜品销量总和与售价的均值为：\n',detail.agg({'counts':np.sum,'amounts':np.mean}))
#使用agg方法求不同字段的不同数目统计量
#此时只需要将字典对应key的values转换为列表，将列表元素转换为多个目标的统计量即可
print('菜品订单详情表的菜品销量总和与售价的总和与均值为:\n',detail.agg({'counts':np.sum,'amounts':[np.sum,np.mean]}))

#自定义函数求两倍的和
def DoubleSum1(data):
    s = np.sum(data)*2
    return s
#axis = 0 沿x轴进行计算
print('订单详情表的菜品销量两倍总和为: \n',detail.agg({'counts':DoubleSum1},axis = 0).head()) #？？？

print('订单详情表的菜品销量与售价的和的两倍为: \n',detail[['counts','amounts']].agg(DoubleSum1))

print('订单详情表分组后前3组每组的均值为: \n',detailGroup.agg(np.mean).head(3))
print('订单详情表分组后前3组每组的标准差为: \n',detailGroup.agg(np.std).head(3))

#使用agg方法对分组数据使用不同的聚合函数
print('订单详情分组前3组每组菜品总数和售价的均值为: \n',detailGroup.agg({'counts':np.sum,'amounts':np.mean}).head(3))


