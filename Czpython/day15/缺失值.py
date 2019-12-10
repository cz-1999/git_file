import pandas as pd
detail = pd.read_csv('D:/python/czpython/detail.csv',index_col=0,encoding='gbk')

#isnull和null的用法
print('detail每个特征缺失的数目: \n',detail.isnull().sum())
print('detail每个特征非缺失的数目: \n',detail.notnull().sum())

#1.删除法
#使用dropna方法删除缺失值
print('去除缺失的列前detail的形状为: ',detail.shape)
print('去除缺失的列后detail的形状为: ',detail.dropna(axis=1,how = 'any').shape)
#当how参数取值为any时删除了一个特征,说明这个特征存在缺失值,若how参数不取any这个默认值而是取all
#则表示整个特征全部为缺失值时才会执行删除操作

#2.替换法
detail1 = detail.fillna(-99) #用-99来填补所有的缺失值
print('detail每个特征缺失的数目为: \n',detail1.isnull().sum())

#3.插值法

#SciPy interpolate模块插值
#线条插值
import numpy as np
from scipy.interpolate import interp1d #是数字1 不是字母l
x = np.array([1,2,3,4,5,8,9,10])#创建自变量x
y1 =np.array([2,8,18,32,50,128,162,200])#创建因变量y1
y2 =np.array([3,5,7,9,11,17,19,21])#创建因变量y2
LinearInsValue1 = interp1d(x,y1,kind='linear')#线性插值拟合为x,y1
LinearInsValue2 = interp1d(x,y2,kind='linear')#线性插值拟合为x,y2
print('当x为6、7时，使用线性插值y1为: ',LinearInsValue1([6,7]))
print('当x为6、7时，使用线性插值y2为: ',LinearInsValue2([6,7]))

#拉格朗日插值
from scipy.interpolate import lagrange
LargeInsValue1 = lagrange(x,y1) #拉格朗日插值x,y1
LargeInsValue2 = lagrange(x,y2) #拉格朗日插值x,y2
print('当x为6、7时，使用拉格朗日插值y1为: ',LargeInsValue1([6,7]))
print('当x为6、7时，使用拉格朗日插值y2为: ',LargeInsValue2([6,7]))

'''
#样条插值
from scipy.interpolate import spline
#样条插值拟合x,y1
SplineInsValuel = spline(x,y1,xnew=np.array([6,7]))#spline函数已经过时，更新为BSpline函数，但是BSpline不知道参数
#样条插值拟合x,y2
SplineInsValue2 = spline(x,y2,xnew=np.array([6,7]))
print('当x为6、7时，使用样条插值y1为: ',SplineInsValuel)
print('当x为6、7时，使用样条插值y2为: ',SplineInsValue2)
'''
#从拟合结果来看，多项式插值和样条插值在两种情况下的拟合都非常出色，线性插值法只在自变量和因变量
#为线性关系的情况下拟合才较为出色(线性：指量与量之间按比例、成直线的关系，
#在数学上可以理解为一阶导数为常数的函数；),而在实际分析中线性关系非常少见，大多数情况下，多项式
#插值和样条插值是较为合适的选择，多项式插值理解为拟合为曲线，样条插值理解为拟合为更为精细的曲线
