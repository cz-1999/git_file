import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei' #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #保证字符正常显示
data = np.load('D:\python\czpython\国民经济核算季度数据.npz') #读入数据
name = data['columns'] #提取columns数组，视为数据的标签
values = data['values'] #提取values数组，视为数据存在的位置）

label = ['第一产业','第二产业','第三产业'] #数组刻度标签
plt.figure(figsize=(6,5)) #设置画布
plt.bar(range(3),values[-1,3:6],width = 0.5)#绘制直方图
plt.xlabel = ('产业')#添加x轴的标签
plt.ylabel = ('国民生产总值（亿元）') #添加y轴标签
plt.xticks(range(3),label)
plt.title('2017年第一季度各产业国民生产总值直方图')#添加图表标题
plt.savefig('D:\python\czpython\save_2017年第一季度各产业国民生产总值直方图.png')
plt.show()

