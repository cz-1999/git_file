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



