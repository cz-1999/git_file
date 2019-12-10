#加载datasets模块中的数据集
#数据集 sklearn自带的一些经典数据的集合

#加载breast_cancer数据集
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()#将数据集赋值给cander变量
print('breast_cander数据集的长度为: ',len(cancer))
print('breast_cander数据集的类型为: ',type(cancer))

#sklearn自带数据集内部信息获取
cancer_data = cancer['data']
print('breast_cancer数据集的数据为: \n',cancer_data)

#取出数据集的标签
cancer_target = cancer['target']
print('breast_cancer数据集的标签为 \n',cancer_target)

#取出数据集的特征名
cancer_names = cancer['feature_names']
print('breast_cancer数据集的特征名为 \n',cancer_names)

#取出数据集的描述信息
cancer_desc = cancer['DESCR']
print('breast_cancer数据集的特征名为 \n',cancer_desc)

#将数据集划分为训练集和测试集
#使用train_test_split划分数据集
print('原始数据集数据的形状为: ',cancer_data.shape)
print('原始数据集标签的形状为: ',cancer_target.shape)

from sklearn.model_selection import train_test_split
cancer_data_train,cancer_data_test,\
cancer_target_train,cancer_target_test = \
train_test_split(cancer_data,cancer_target,\
test_size = 0.2,random_state=42)
print('训练集数据的形状为: ',cancer_data_train.shape)
print('训练集标签的形状为: ',cancer_target_train.shape)
print('测试集数据的形状为: ',cancer_data_test.shape)
print('测试集标签的形状为: ',cancer_target_test.shape)

#使用sklearn转换器进行数据预处理与降维
#离散标准化
import numpy as np
from sklearn.preprocessing import MinMaxScaler
Scaler = MinMaxScaler().fit(cancer_data_train)#生成规则
#将规则应用于训练集
cancer_trainScaler = Scaler.transform(cancer_data_train)
#将规则应用于测试集
cancer_testScaler = Scaler.transform(cancer_data_test)
print('离差标准化前训练数据的最小值为: ',np.min(cancer_data_train))
print('离差标准化后训练数据的最小值为: ',np.min(cancer_trainScaler))
print('离差标准化前训练数据的最大值为: ',np.max(cancer_data_train))
print('离差标准化后训练数据的最大值为: ',np.max(cancer_trainScaler))
print('离差标准化前训练数据的最小值为: ',np.min(cancer_data_test))
print('离差标准化后训练数据的最小值为: ',np.min(cancer_testScaler))
print('离差标准化前训练数据的最大值为: ',np.max(cancer_data_test))
print('离差标准化后训练数据的最大值为: ',np.max(cancer_testScaler))

#PCA降维  减少数据集的列数

#对breast_cancer数据集进行PCA降维
#特征维度为10
from sklearn.decomposition import PCA
pca_model = PCA(n_components=10).fit(cancer_trainScaler)#生成规则
#将规则应用于训练集
cancer_trainPca = pca_model.transform(cancer_trainScaler)
#将规则应用于测试集
cancer_testPca = pca_model.transform(cancer_testScaler)
print('PCA降维前训练集数据的形状为: ',cancer_trainScaler.shape)
print('PCA降维后训练集数据的形状为: ',cancer_trainPca.shape)
print('PCA降维前测试集数据的形状为: ',cancer_testScaler.shape)
print('PCA降维前测试集数据的形状为: ',cancer_testPca.shape)

#使用sklearn实现数据处理和降维
#获取sklearn自带的boston数据集
from  sklearn.datasets import load_boston
boston = load_boston()
boston_data = boston['data']
boston_target = boston['target']
boston_names = boston['feature_names']
print('boston数据集数据的形状为: ',boston_data.shape)
print('boston数据集标签的形状为: ',boston_target.shape)
print('boston数据集特征名的形状为: ',boston_names.shape)

#将数据集划分为训练集和测试集
from sklearn.model_selection import train_test_split
boston_data_train,boston_data_test,\
    boston_target_train,boston_target_test = \
train_test_split(boston_data,boston_target,test_size=0.2,random_state=42)
print('训练集数据的形状为: ',boston_data_train.shape)
print('训练集标签的形状为: ',boston_target_train.shape)
print('测试集数据的形状为: ',boston_data_test.shape)
print('测试集标签的形状为: ',boston_target_test.shape)

#使用转换器进行数据预处理
#使用stdScale.transform进行数据预处理

from sklearn.preprocessing import StandardScaler
stdScale = StandardScaler().fit(boston_data_train)#生成规则

#将规则应用于训练集
boston_trainScaler = stdScale.transform(boston_data_train)
#将规则应用于测试集
boston_testScaler = stdScale.transform(boston_data_test)
print('标准差标准化后训练集数据的方差为: ',np.var(boston_trainScaler))
print('标准差标准化后训练集数据的均值为: ',np.mean(boston_trainScaler))
print('标准差标准化后测试集数据的方差为: ',np.var(boston_testScaler))
print('标准差标准化后测试集数据的均值为: ',np.mean(boston_testScaler))

#利用转换器进行PCA降维
#利用pca.transform分别对训练集和测试集进行PCA降维

from sklearn .decomposition import PCA
#生成规则
pca = PCA(n_components=5).fit(boston_trainScaler)
#将规则应用于训练集
boston_trainPca = pca.transform(boston_trainScaler)
#将规则应用于测试集
boston_testPca = pca.transform(boston_testScaler)
print('降维后boston数据集数据测试集的形状为: ',boston_testPca.shape)
print('降维后boston数据集数据训练集的形状为: ',boston_trainPca.shape)


