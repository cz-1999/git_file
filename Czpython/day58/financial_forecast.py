#分析财政收入数据特征的相关性
import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso,LassoCV,LassoLarsCV
inputfile = 'D:/python/czpython/data.csv'#输入数据文件
data = pd.read_csv(inputfile)#读入数据,存为dataframe形式
#保留两位小数,np.round()函数，np.round(dataframe,n)四舍五入函数,n决定保留几位小数
print('相关性系数矩阵为；',np.round(data.corr(method='pearson'),2))

#使用lasso回归选取财政收入预测的关键特征
lasso = Lasso(1000,random_state=1234)#调用lasso函数
lasso.fit(data.iloc[:,0:13],data['y'])
print('相关系数为: ',np.round(lasso.coef_,5))#输出结果，四舍五入保留5为小数
#计算相关系数非0的个数,np.sum()函数里面还可以传入表达式
print('相关系数非0的个数为:',np.sum(lasso.coef_!=0))
mask = lasso.coef_!=0 #返回一个相关系数是否为0的布尔数组
print('相关系数是否为0',mask)
outputfile = 'D:/python/czpython/new_reg_data.csv' #输出的数据文件
new_reg_data = data.iloc[:,mask] #返回相关系数非0的数据
new_reg_data.to_csv(outputfile)#存储数据
print('输出数据的维度为:',new_reg_data.shape)#查看输出数据的维度

#利用灰色预测和SVR构建财政收入预测模型

#财政收入灰色预测
import numpy as np
import pandas as pd
from day59 import GM11 #引入自编的灰色预测函数
inputfile = 'D:/python/czpython/new_reg_data.csv' #输入的数据文件
inputfile1 = 'D:/python/czpython/data.csv' #输入的数据文件
new_reg_data = pd.read_csv(inputfile) #读取经过特征选着后的数据
data  = pd.read_csv(inputfile1 )#读取总的数据
print(new_reg_data)
new_reg_data.index = range(1994,2014) #修改dataframe的行索引
new_reg_data.loc[2014] = None #增加两个空白行
new_reg_data.loc[2015] = None
l = ['x1','x3','x4','x5','x6','x7','x8','x13']
for i in l:
    f = GM11.GM11(new_reg_data.loc[range(1994,2014),i].as_matrix())[0] #返回的是灰色预测函数 as_matrix()的作用?????
    new_reg_data.loc[2014,i] = f(len(new_reg_data)-1) #2014年预测结果,灰色预测函数的参数为所在行的高度, ????????
    new_reg_data.loc[2015,i] = f(len(new_reg_data)) #2015年预测结果
    new_reg_data[i] = new_reg_data[i].round(2) #保留两位小数
outputfile = 'D:/python/czpython/new_reg_data_GM11.xls' #灰色预测后的保存路径
y = list(data['y'].values) #提取财政收入列，合并至新数据框中
#新数据框的行数比y列多了两行，所以y要向下扩展两个值才能合并至新数据框中
y.extend([np.nan,np.nan]) # y往下扩展了2个值，值为空
new_reg_data['y'] = y
new_reg_data.to_excel(outputfile)
print('预测结果为: ',new_reg_data.loc[2014:2015,:])#预测结果展示  Unnamed: 0列在新扩展的两行中没有值所以为nan


#财政收入支持向量回归预测模型
import pandas as pd
from sklearn.svm import LinearSVR
import matplotlib.pyplot as plt
from sklearn.metrics import explained_variance_score,mean_absolute_error,mean_squared_error,median_absolute_error,r2_score
inputfile = 'D:/python/czpython/new_reg_data_GM11.xls' #灰色预测后的保存路径

data = pd.read_excel(inputfile)
data.index = range(1994,2016) #读取数据之后，数据的行索引发生变化，要更改数据的行索引
feature = ['x1','x3','x4','x5','x6','x7','x8','x13']
data_train = data.loc[range(1994,2014)].copy() #取2014年以前的数据建模
data_mean = data_train.mean()
data_std = data_train.std()
data_train = (data_train - data_mean)/data_std #数据标准化
x_train = data_train[feature].as_matrix() #特征数据 dataframe的as_matrix属性，将dataframe转换为多维矩阵
y_train = data_train['y'].as_matrix() #标签数据
linearsvr = LinearSVR() #调用LinearSVR函数
linearsvr.fit(x_train,y_train) #创建模型
x = ((data[feature] - data_mean[feature])/data_std[feature]).as_matrix() #不能使用x_train，x_train是2014年之前的数据，
#需要2014,2015年的数据（灰度预测模型得出的），对2014,2015年的生产总值进行预测
data[u'y_pred'] = linearsvr.predict(x) * data_std['y']+data_mean['y']#预测并还原结果 还原结果????
#SVR预测后保存的结果
outputfile = 'D:/python/czpython/new_reg_data_GM11_revenue.xls'
data.to_excel(outputfile)
print('真实值与预测值分别为:',data[['y','y_pred']])

#pd.dataframe.plot绘图函数
print('预测图为：',data[['y','y_pred']].plot(subplots = True,
      style=['b-o','r-*']))
plt.show()
