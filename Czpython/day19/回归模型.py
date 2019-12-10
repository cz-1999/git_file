#构建并评价回归模型
#使用sklearn估计器构建线性回归模型
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
#加载boston数据
boston = load_boston()
x = boston['data']
y = boston['target']
names = boston['feature_names']
#将数据划分为训练集和测试集
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size= 0.2,random_state=125) #test_size传入可为int,或float, int型要是
#绝对数目，float型需要在0-1之间代表测试集的大小，一般test_size和train_size只能传入一个，但是因为版本原因，有时要传入两个不然会报错，random_state
#代表随机种子编号，随机分数据，编号相同产生的结果相同
#建立线性回归模型
clf = LinearRegression().fit(x_train,y_train)
print('建立的LinearRegression模型为: \n',clf)
#预测测试集结果
y_pred = clf.predict(x_test)
print('预测前20个结果为: \n',y_pred[:20])
#回归结果可视化
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif'] = 'SimHei'
fig =plt.figure(figsize=(10,6))#设定空白画布，并定制大小
plt.plot(range(y_test.shape[0]),y_test,color='blue',linewidth=1.5,linestyle='-')
plt.plot(range(y_test.shape[0]),y_pred,color='red',linewidth=1.5,linestyle='-.')
plt.xlim((0,102));plt.ylim((0,55))
plt.legend(['真实值','预测值'])
plt.savefig('D:/python/czpython/save_聚类回归结果.png')
plt.show()
#回归模型评价
from sklearn.metrics import explained_variance_score,mean_absolute_error,mean_squared_error,median_absolute_error,r2_score
print('Boston数据线性回归模型的平均绝对误差为: ',mean_absolute_error(y_test,y_pred))
print('Boston数据线性回归模型的均方误差为: ',mean_squared_error(y_test,y_pred))
print('Boston数据线性回归模型的中值绝对误差为: ',median_absolute_error(y_test,y_pred))
print('Boston数据线性回归模型的可解释方差为: ',explained_variance_score(y_test,y_pred))
print('Boston数据线性回归模型的R^2值为: ',r2_score(y_test,y_pred))

#房子估值
#使用sklearn估计其构建线性回归模型为

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
house = pd.read_csv('D:/python/czpython/cal_housing.data',sep = ',')
house_data =house.iloc[:,:-1]
house_target = house.iloc[:,-1]
#没有用
#house_names = ['longitude','latitude','housingMedianAge','totalRooms','totalBedrooms','population','households','medianIncome']
house_train,house_test,house_target_train,house_target_test = train_test_split(house_data,house_target,test_size=0.2,random_state=42)
GBR_house = GradientBoostingRegressor().fit(house_train,house_target_train)
print('建立的梯度提升回归模型为: \n',GBR_house)

#评价构建的线性回归模型
house_traget_pred = GBR_house.predict(house_test)
print('数据梯度提升回归模型的平均绝对误差为: ',mean_absolute_error(house_target_test,house_traget_pred))#利用测试集已知标签和测试集数据预测的标签
print('数据梯度提升回归模型的均方误差为: ',mean_squared_error(house_target_test,house_traget_pred))
print('数据梯度提升回归模型的中值绝对误差为: ',median_absolute_error(house_target_test,house_traget_pred))
print('数据梯度提升回归模型的可解释方差为: ',explained_variance_score(house_target_test,house_traget_pred))
print('数据梯度提升回归模型的R^2值为: ',r2_score(house_target_test,house_traget_pred))
