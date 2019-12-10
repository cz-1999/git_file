import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei' #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #保证字符正常显示
data = np.load('D:\python\czpython\国民经济核算季度数据.npz') #读入数据
name = data['columns'] #提取columns数组，视为数据的标签
values = data['values'] #提取values数组，视为数据存在的位置）

label = ['第一产业','第二产业','第三产业'] #定义标签
gdp = (list(values[:,3]),list(values[:,4]),list(values[:,5]))
plt.figure(figsize=(8,7))
plt.boxplot(gdp,notch=True,labels= label,meanline = True)#绘制箱线图
plt.title('2000-2017年各产业国民生产总值箱线图')
plt.savefig('D:\python\czpython\save_2017年第一季度各产业生产总值箱线图.png')
plt.show()