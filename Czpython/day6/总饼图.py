import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei' #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #保证字符正常显示
data = np.load('D:\python\czpython\国民经济核算季度数据.npz') #读入数据
name = data['columns'] #提取columns数组，视为数据的标签
values = data['values'] #提取values数组，视为数据存在的位置）

label1 = ['第一产业','第二产业','第三产业']#刻度标签1
label2 = ['农业','工业','建筑','批发','交通','餐饮','金融','房地产','其他']#刻度标签2
explode1 = [0.01,0.01,0.01]
explode2 = [0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01]
p =plt.figure(figsize = (12,12))#设置画布
#子图1
ax1 = p.add_subplot(2,2,1)
plt.pie(values[0,3:6],explode= explode1,labels = label1,autopct='%1.1f%%')#绘制饼图
plt.title('2000年第一季度国民生产总值产业构成分布饼图')
#子图2
ax2 = p.add_subplot(2,2,2)
plt.pie(values[-1,3:6],explode= explode1,labels = label1,autopct='%1.1f%%')#绘制饼图
plt.title('2017年第一季度国民生产总值产业构成分布饼图')
#子图3
ax3 = p.add_subplot(2,2,3)
plt.pie(values[0,6:],explode= explode2,labels = label2,autopct='%1.1f%%')#绘制饼图
plt.title('2000年第一季度国民生产总值行业构成分布饼图')
#子图4
ax4 = p.add_subplot(2,2,4)
plt.pie(values[-1,6:],explode= explode2,labels = label2,autopct='%1.1f%%')#绘制饼图
plt.title('2017年第一季度国民生产总值行业构成分布饼图')
plt.savefig('D:\python\czpython\save_国民生产总值构成分布饼图.png')
plt.show()