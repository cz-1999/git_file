import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei' #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #保证字符正常显示
data = np.load('D:\python\czpython\国民经济核算季度数据.npz') #读入数据
name = data['columns'] #提取columns数组，视为数据的标签
values = data['values'] #提取values数组，视为数据存在的位置）

label1 = ['第一产业','第二产业','第三产业']#刻度标签1
label2 = ['农业','工业','建筑','批发','交通','餐饮','金融','房地产','其他']#刻度标签2

gdp1 = (list(values[:,3]),list(values[:,4]),list(values[:,5]))
gdp2 = ([list(values[:,i])for i in range(6,15)])
p = plt.figure(figsize=(8,8))
#子图1
ax1 = p.add_subplot(2,1,1)
#绘制箱线图
plt.boxplot(gdp1,notch=True,labels= label1,meanline=True)
plt.title('2000-2017年各产业国民生产总值箱线图')
plt.ylabel('生产总值（亿元）')#添加y轴名称
#子图2
ax2 = p.add_subplot(2,1,2)
#绘制箱线图
plt.boxplot(gdp2,notch=True,labels= label2,meanline=True)
plt.title('2000-2017年各行业国民生产总值箱线图')
plt.xlabel('行业')
plt.ylabel('生产总值（亿元')
plt.savefig('D:\python\czpython\save_国民生产总值分散情况箱线图.png')
plt.show()