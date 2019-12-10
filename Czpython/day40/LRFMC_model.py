
#缺失值与异常值处理
import numpy as np
import pandas as pd
airline_data = pd.read_csv("D:/python/czpython/air_data.csv",encoding="gb18030")#导入航空数据
print(airline_data.shape) #原始数据的形状为
#去除票价为空的记录
exp1 = airline_data["SUM_YR_1"].notnull()   #返回的应该是符合条件的行索引
exp2 = airline_data["SUM_YR_2"].notnull()   #SUM_YR_1，SUM_YR_2 应该代指两个票价的累计和
exp = exp1 & exp2
airline_notnull = airline_data.loc[exp,:]   #取出符合条件的数据
print('删除缺失纪录后数据的形状为: ',airline_notnull.shape)
#只保留票价非0的，或者平均折扣率不为0，且总飞行千米数大于0的纪录
index1 = airline_notnull['SUM_YR_1'] != 0
index2 = airline_notnull['SUM_YR_2'] != 0
index3 = (airline_notnull['SEG_KM_SUM']>0)&(airline_notnull['avg_discount']!=0)
airline = airline_notnull[(index1|index2)&index3]
print('删除异常纪录后数据的形状为:',airline.shape)

#选取并构建LRFMC模型的5个特征
#选取需求特征 LRFMC特征中的R，F，M，C这4个特征直接提取即可使用,L特征则需要另作计算
airline_selection = airline[["FFP_DATE","LOAD_TIME","FLIGHT_COUNT","LAST_TO_END","avg_discount","SEG_KM_SUM"]]
#构建L特征
L = pd.to_datetime(airline_selection["LOAD_TIME"])-pd.to_datetime(airline_selection["FFP_DATE"]) #相减之后得出的是天数
L = L.astype("str").str.split().str[0]  #将L转换为字符串格式，用字符串分割出天数
L = L.astype("int")/30  #将天数粗略的转换成月数
print(L)
#合并特征
airline_features = pd.concat([L,airline_selection.iloc[:,2:]],axis=1)
print('构建的LRFMC特征前5行为:\n',airline_features.head())
#标准化LRFMC模型的特征
#标准化可以使用sklearn的preprocessing模块，也可以使用自定义函数的方法实现
from sklearn.preprocessing import StandardScaler
data = StandardScaler().fit_transform(airline_features)
np.savez('D:/python/czpython/airline_scale.npz',data)
print('标准化后的LRFMC模型的5个特征为: \n',data[:5,:])

#KMeans函数语法与参数
#sklearn的cluster模块提供KMeans函数来构建KMeans聚类模型

#用K-Means聚类算法对客户数据进行客户分群，聚成5类（需要结合业务的理解与分析来确定客户的类别数量）
import numpy as np
from sklearn.cluster import KMeans #导入K-Means算法
airline_scale = np.load('D:/python/czpython/airline_scale.npz')['arr_0']  #????
k = 5
#构建模型
kmeans_model = KMeans(n_clusters=k,n_jobs=4,random_state=123)
fit_kmeans = kmeans_model.fit(airline_scale)#模型训练
print('\n',kmeans_model.cluster_centers_) #查看聚类中心
print('\n',kmeans_model.labels_) #查看样本类别标签
#统计不同样本标签的数目
r1 = pd.Series(kmeans_model.labels_).value_counts()
print(r1)







