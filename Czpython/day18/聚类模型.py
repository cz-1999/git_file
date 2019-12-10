#使用sklearn估计器构建K-Means聚类模型
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

iris = load_iris()
iris_data = iris['data']#提取数据中的特征
iris_target = iris['target']#提取数据中的标签
iris_names = iris['feature_names']#提取特征名
scale = MinMaxScaler().fit(iris_data)#训练规则，离差标准化，先对数据进行预处理
iris_dataScale = scale.transform(iris_data)#应用规则，数据标准化
kmeans = KMeans(n_clusters= 3,random_state=123).fit(iris_dataScale)#构建并训练模型
print('构建的K-Means模型为: \n',kmeans)
result = kmeans.predict([[1.5,1.5,1.5,1.5]])
print('花萼花瓣长度宽度全为1.5的鸢尾花预测类别为: ',result[0])#0可能是一个类别

#聚类结果可视化
import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
#使用TSNE进行降维，降成两维
tsne = TSNE(n_components=2,init='random',random_state=177).fit(iris_data)
df = pd.DataFrame(tsne.embedding_)#将原始数据转换为dataframe
df['labels'] = kmeans.labels_#将聚类结果存进df数据表
#提取不同标签的数据
df1 = df[df['labels']==0]
df2 = df[df['labels']==1]
df3 = df[df['labels']==2]
#绘制图形
fig = plt.figure(figsize=(9,6))#设置空白画布,并制定大小
#用不同的颜色绘制不同的数据
plt.plot(df1[0],df1[1],'bo',df2[0],df2[1],'r*',df3[0],df3[1],'gD')
plt.savefig('D:/python/czpython/save_聚类结果.png')
#plt.show()

#评价聚类模型
#使用FMI评价法评价K-Means聚类模型
from sklearn.metrics import fowlkes_mallows_score
for i in range(2,7):
    #构建并训练模型
    kmeans = KMeans(n_clusters=i,random_state=123).fit(iris_data)
    score = fowlkes_mallows_score(iris_target,kmeans.labels_)
    print('iris数据聚%d类FMI评分分值为：%f'%(i,score))

#使用轮廓系数评价法评价K-Means聚类模型
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
silhouettteScore =[]
for i in range(2,15):
    #构建并训练模型
    kmeans = KMeans(n_clusters=i,random_state=123).fit(iris_data)
    score = silhouette_score(iris_data,kmeans.labels_)
    silhouettteScore.append(score)
plt.figure(figsize=(10,6))
plt.plot(range(2,15),silhouettteScore,linewidth=1.5,linestyle='-')
#plt.show()

#使用Calinski-Harabasz指数评价K-Means聚类模型
from sklearn.metrics import calinski_harabaz_score
for i in range(2,7):
    #构建并训练模型
    kmeans =KMeans(n_clusters=i,random_state=123).fit(iris_data)
    score = calinski_harabaz_score(iris_data,kmeans.labels_)
    print('iris数据聚%d类calinski_harabaz指数为：%f'%(i,score))
#聚类数目为3时得分最高,所以可以认为iris数据聚类为3类的时候效果最优

#任务实现
#构建K-Means聚类模型
#对Seeds构建K-Means聚类模型
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
seeds = pd.read_csv('D:/python/czpython/seeds_dataset.txt',sep='\t')
print('数据集的形状为: ',seeds.shape)
#处理数据
seeds_data = seeds.iloc[:,:7].values
seeds_target = seeds.iloc[:,7].values
seeds_names = seeds.columns[:7]
stdScale = StandardScaler().fit(seeds_data)
seeds_dataScale = stdScale.transform(seeds_data)
#构建并训练模型
kmeans = KMeans(n_clusters=3,random_state=42).fit(seeds_data)
print('构建的K-Means模型为: \n',kmeans)

#评价构建的K-Means聚类模型
from sklearn.metrics import calinski_harabaz_score
for i in range(2,7):
    #构建并训练模型
    kmeans = KMeans(n_clusters = i,random_state=123).fit(seeds_data)
    score = calinski_harabaz_score(seeds_data,kmeans.labels_)
    print('seeds数据聚%d类calinski_harabaz_score指数为: %f'%(i,score))
