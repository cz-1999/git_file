import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] =  'SimHei' #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #确保字符显示正常
data = np.load("D:\python\czpython\国民经济核算季度数据.npz")
name = data['columns']#提取其中的columns数组，视为数组的标签
values = data['values']#提取其中的values数组，视为数组的存在位置

p = plt.figure(figsize=(12,12))#设置画布
#子图1
ax1 = p.add_subplot(2,1,1) #创建一个两行一列的子图，第一幅图
plt.scatter(values[:,0],values[:,3],marker='o',c='r')#绘制散点图
plt.scatter(values[:,0],values[:,4],marker='D',c='b')#绘制散点图
plt.scatter(values[:,0],values[:,5],marker='v',c='y')#绘制散点图
plt.ylabel('生产总值（亿元')#添加纵轴标签
plt.title('2000-2017年各产业与行业各季度国民生产总值散点图')#添加标题
plt.legend(['第一产业','第二产业','第三产业'])#添加图例
#子图2
ax2 = p.add_subplot(2,1,2)
plt.scatter(values[:,0],values[:,6],marker='o',c='r')#绘制散点图
plt.scatter(values[:,0],values[:,7],marker='D',c='b')#绘制散点图
plt.scatter(values[:,0],values[:,8],marker='v',c='y')#绘制散点图
plt.scatter(values[:,0],values[:,9],marker='8',c='g')#绘制散点图
plt.scatter(values[:,0],values[:,10],marker='p',c='c')#绘制散点图
plt.scatter(values[:,0],values[:,11],marker='+',c='m')#绘制散点图
plt.scatter(values[:,0],values[:,12],marker='s',c='k')#绘制散点图
plt.scatter(values[:,0],values[:,13],marker='*',c='purple')#绘制散点图
plt.scatter(values[:,0],values[:,14],marker='d',c='brown')#绘制散点图
plt.legend(['农业','工业','建筑','批发','交通','餐饮','金融','房地产','其他'])
plt.xlabel('年份')#添加横轴标签
plt.ylabel('生产总值（亿元')#添加纵轴标签
plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation=45)
plt.savefig('D:\python\czpython\save_2000-2017年各产业与行业各季度国民生产总值散点子图.png')
plt.show()