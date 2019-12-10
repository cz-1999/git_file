import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] =  'SimHei' #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #确保字符显示正常
data = np.load("D:\python\czpython\国民经济核算季度数据.npz")
name = data['columns']#提取其中的columns数组，视为数组的标签
values = data['values']#提取其中的values数组，视为数组的存在位置

plt.figure(figsize = (8,7))#设置画布
plt.plot(values[:,0],values[:,2],color = 'r',linestyle = '--')
plt.xlabel('年份')#添加横轴标签
plt.ylabel('生产总值（亿元)')#添加y轴名称
plt.ylim(0,225000) #少加个0，图只能画出来一点
plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation=45)
plt.title('2000-2017年各季度国民生产总值折线图')#添加图表标题
plt.savefig('D:\python\czpython\save_2000-2017年季度国民生产总值折线图.png')
#plt.show()

plt.figure(figsize = (8,7))#设置画布
plt.plot(values[:,0],values[:,2],color = 'r',linestyle = '--',marker = 'o')
plt.xlabel('年份')#添加横轴标签
plt.ylabel('生产总值（亿元)')#添加y轴名称
plt.ylim(0,225000) #少加个0，图只能画出来一点
plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation=45)
plt.title('2000-2017年各季度国民生产总值点线图')#添加图表标题
plt.savefig('D:\python\czpython\save_2000-2017年季度国民生产总值点线图.png')
#plt.show()

plt.figure(figsize = (8,7))#设置画布
#绘制折线图1
plt.plot(values[:,0],values[:,3],color = 'r',linestyle = '--')
#绘制折线图2
plt.plot(values[:,0],values[:,4],color = 'y',linestyle = '-')
#绘制折线图3
plt.plot(values[:,0],values[:,5],color = 'k',linestyle = '-.')
plt.xlabel('年份')#添加横轴标签
plt.ylabel('生产总值（亿元）')#添加纵轴标签
plt.ylim((0,225000))
plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation = 45)
plt.title('2000-2017年各产业季度国民生产总值折线图')
plt.savefig('D:\python\czpython\save_2000-2017年各产业季度国民生产总值折线图.png')
plt.show()