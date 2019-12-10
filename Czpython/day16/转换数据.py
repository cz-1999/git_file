import numpy as np
import pandas as pd
detail = pd.read_csv('D:/python/czpython/detail.csv',encoding='gbk')

#哑变量处理类别型数据
#哑变量处理示例

data = detail.loc[0:5,'dishes_name'] #抽取部分数据做演示
print('哑变量处理前的数据为: \n',data)
print('哑变量处理后的数据为: \n',pd.get_dummies(data))

#离散化连续型数据
#1.等宽法,cut函数，将数据的值域分成具有相同宽度的区间

#等宽法离散化示例
price = pd.cut(detail['amounts'],5)
print('离散化后5条纪录售价分布为: \n',price.value_counts())

#2.等频法
#cut函数不能够直接使用等频法，但可以定义将相同数量的纪录放进每一个区间


#等频法离散化示例
#自定义等频法离散化函数
def SameRateCut(data,k):
    w = data.quantile(np.arange(0,1+1.0/k,1.0/k))
    data = pd.cut(data,w)
    return data
#对菜品售价进行等频法离散化
result = SameRateCut(detail['amounts'],5).value_counts()
print('菜品数据等频法离散化后各个类别数目分布状况为: \n',result)






#聚类分析法
#基于聚类分析的离散化
#自定义数据K-Means聚类离散化函数
def KmeanCut(data,k):
    from sklearn.cluster import KMeans
    #引入K-Means,建立模型
    kmodel = KMeans(n_clusters=k)
    kmodel.fit(data.values.reshape((len(data),1)))
    #训练模型 输出聚类中心并排序
    c=pd.DataFrame(kmodel.cluster_centers_).sort_values(0)
    w=c.rolling(2).mean().iloc[1:]#相邻两项求中点，作为边界点
    w=[0]+list(w[0])+[data.max()]#把首末边界点加上
    data =pd.cut(data,w)
    return data
#菜品售价聚类分析离散化
result = KmeanCut(detail['amounts'],5).value_counts()
print('菜品售价聚类离散化后各个类别数目分布状况为：\n',result)

#任务实现
#对菜品dishes_name哑变量处理
data = detail.loc[:,'dishes_name']
print('哑变量处理前的数据为: \n',data.iloc[:5])
print('哑变量处理后的数据为: \n',pd.get_dummies(data).iloc[:5,:5])

#菜品售价等频法离散化
def SameRateCut(data,k):
    w = data.quantile(np.arange(0,1+1.0/k,1.0/k))
    data = pd.cut(data,w)
    return data
#对菜品售价进行等频法离散化
result = SameRateCut(detail['amounts'],5).value_counts()
print('菜品数据等频法离散化后各个类别数目分布状况为: \n',result)