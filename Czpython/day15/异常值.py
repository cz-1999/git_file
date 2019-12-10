import numpy as np
import pandas as pd
detail = pd.read_csv('D:/python/czpython/detail.csv',index_col=0,encoding='gbk')

#定义拉依达准则来识别异常值函数

def outRange(Ser1):                          #\表示对下一行来说继续上一行的内容
    boolInd = (Ser1.mean()-3*Ser1.std()>Ser1)|\
    (Ser1.mean()+3*Ser1.std()<Ser1)  #python中的缩进格式很严格，该对齐的要对齐
    index = np.arange(Ser1.shape[0])[boolInd]
    outRange = Ser1.iloc[index]
    return outRange
outlier = outRange(detail['counts'])
print('使用3o原则判定异常值的个数为: ',outlier.shape[0])
print('异常值的最大值为: ',outlier.max())
print('异常值的最小值为: ',outlier.min())

#boolInd等于在3o原则之外的数据，不知道是什么格式
#index 等于 异常数据的索引 index = np.arange(Ser1.shape[0])[boolInd]理解为 为Ser1中的所有数据都添加上下标
#然后把异常数据的下标取出来
#拉依达原则具有一定的局限性，即此原则只对正态分布或进正态分布的数据有效，对其他分布类型的数据无效

#箱线图分析
import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
p = plt.boxplot(detail['counts'].values,notch=True)#画出箱线图
outlier1 =p['fliers'][0].get_ydata()  #fliers为异常值标签
plt.savefig('D:/python/czpython/save_菜品异常数据识别.png')
#plt.show()
print('销售数据异常值个数为: ',len(outlier1))
print('销售数据异常值最大值为:',max(outlier1))
print('销售数据异常值最小值为:',min(outlier1))

#任务实现

#订单详情表的样本去重与特征去重
print('进行去重操作前订单详情表的形状:',detail.shape)
#样本去重
detail.drop_duplicates(inplace=True)
#特征去重
#订单详情表缺失值的检测与处理
naRate = (detail.isnull().sum()/ \
    detail.shape[0] * 100).astype('str')+'%' #为什么要乘以100，因为后面有一个%号
print('每个特征的缺失率为: \n',naRate)

#删除全部数据均为缺失的列
detail.dropna(axis=1,how='all',inplace=True)
print('经过缺失值处理后订单详情表各特征缺失值的数目为: \n',detail.isnull().sum())
#3.处理菜品销售数据异常值
#订单详情表异常值检测与处理
#定义异常值识别与处理函数
def outRange(Ser1):
    QL  = Ser1.quantile(0.25)
    QU  = Ser1.quantile(0.75)
    IQR = QU - QL
    Ser1.loc[Ser1>(QU+1.5*IQR)] = QU##?????
    Ser1.loc[Ser1<(QL-1.5*IQR)] = QL
    return Ser1

#处理销售量和售价的异常值
detail['counts'] = outRange(detail['counts'])
detail['amounts'] = outRange(detail['amounts'])
#查看处理后的销售量，售价的最小值，最大值
print('销售量的最小值为: \n',detail['counts'].min())
print('销售量的最大值为: \n',detail['counts'].max())
print('售价的最小值为: \n',detail['amounts'].min())
print('售价的最大值为: \n',detail['amounts'].max())


