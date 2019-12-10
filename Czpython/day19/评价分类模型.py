#使用sklearn估计器构建SVM模型
#加载所需函数
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
cancer = load_breast_cancer()
cancer_data = cancer['data']
cancer_target = cancer['target']
cancer_names = cancer['feature_names']
#将数据集分为训练集和测试集
cancer_data_train,cancer_data_test,\
cancer_target_train,cancer_target_test = \
train_test_split(cancer_data,cancer_target,test_size=0.2,random_state=22)
#数据标准化
stdScaler = StandardScaler().fit(cancer_data_train)
cancer_trainStd = stdScaler.transform(cancer_data_train)
cancer_testStd = stdScaler.transform(cancer_data_test)
#建立SVM模型
svm = SVC().fit(cancer_trainStd,cancer_target_train)
print('建立的SVM模型为: ',svm)
#预测训练集的结果为
cancer_target_pred = svm.predict(cancer_testStd)
print('预测前20个结果为:',cancer_target_pred[:20])
#分类结果的混淆矩阵与准确率
#求出预测和真实一样的数目
true = np.sum(cancer_target_pred == cancer_target_test)
print('预测对的结果数目为: ',true)
print('预测错的结果数目为: ',cancer_target_test.shape[0]-true)
print('预测二的准确率为: ',true/cancer_target_test.shape[0])

#分类模型常用评价方法
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,cohen_kappa_score
print('使用SVM预测breast_cancer数据的准确率: ',accuracy_score(cancer_target_test,cancer_target_pred))
print('使用SVM预测breast_cancer数据的精确率: ',precision_score(cancer_target_test,cancer_target_pred))
print('使用SVM预测breast_cancer数据的召回率: ',recall_score(cancer_target_test,cancer_target_pred))
print('使用SVM预测breast_cancer数据的F1值: ',f1_score(cancer_target_test,cancer_target_pred))
print('使用SVM预测breast_cancer数据的Cohens Kappa系数为: ',cohen_kappa_score(cancer_target_test,cancer_target_pred))

#分类模型评价报告
from sklearn.metrics import classification_report
print('使用SVM预测breast_cancer数据的分类报告为: \n',classification_report(cancer_target_test,cancer_target_pred))
#绘制ROC曲线
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
#求出ROC曲线的x轴和y轴
fpr,tpr,thresholds = \
roc_curve(cancer_target_test,cancer_target_pred)
plt.figure(figsize=(10,6))
plt.xlim(0,1)#设定x轴的范围
plt.ylim(0.0,1.1)#设定y轴的范围
plt.xlabel('False Postive Rate')
plt.ylabel('True Postive Rate')
plt.plot(fpr,tpr,linewidth=2,color='red')
#plt.show()

#鲍鱼年龄预测
import pandas as pd
from sklearn.svm import SVC
abalone = pd.read_csv('D:/python/czpython/abalone.data',sep = ',')#导入数据,要加上sep，不然会报错
abalone_data = abalone.iloc[:,:8]#提取数据
abalone_target = abalone.iloc[:,8]#提取标签
#哑变量处理
sex = pd.get_dummies(abalone_data['sex']) #这一列不是数值型,哑变量处理
abalone_data = pd.concat([abalone_data,sex],axis=1)#连接
abalone_data.drop('sex',axis = 1,inplace = True)#删除原来的那一列
#划分训练集，测试集
abalone_train,abalone_test,\
abalone_target_train,abalone_target_test = \
train_test_split(abalone_data,abalone_target,train_size=0.8,test_size=0.2,random_state=42) #要加上test_size=0.2不然会报错
#一般train_size和test_size只能传入一个，但是因为版本原因又是需要传入两个
#标准化
#转化数据类型
abalone_train = abalone_train.astype('float64')#将dataframe中的数值型由int型 转为 float64型
abalone_test = abalone_test.astype('float64')

stdScaler = StandardScaler().fit(abalone_train)#利用训练集的数据生成规则，离差标准化规则只使用于float64型
abalone_std_train = stdScaler.transform(abalone_train)#将规则应用于训练集
abalone_std_test = stdScaler.transform(abalone_test)#将规则应用于测试集
#建模
svm_abalone = SVC().fit(abalone_std_train,abalone_target_train)
print('建立的SVM模型为: \n',svm_abalone)

#评价构建的SVM分类模型
abalone_target_pred = svm_abalone.predict(abalone_std_test)
print('abalone数据集的SVM分类报告为: \n',classification_report(abalone_target_test,abalone_target_pred))

#会有一个警告，遇到这个问题的原因通常是，在预测的标签中缺少实际的标签，例如实际标签围为 1，1，1，1，0，0，0
#预测标签为0，0，0，0，0这个不是错误



