import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] =  'SimHei' #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #确保字符显示正常
data = np.load("D:\python\czpython\国民经济核算季度数据.npz")
name = data['columns']#提取其中的columns数组，视为数组的标签
values = data['values']#提取其中的values数组，视为数组的存在位置

#保存多个文件时，提取的数组名是什么？

print(name)
print(values)
plt.figure(figsize=(8,7))#设置画布，8 行的长度，7列的长度
plt.scatter(values[:,0],values[:,2],marker = 'o')#绘制散点图
#索引的返回值是数组，values[:,0]索引所有行的第一列，values[:,0]x轴对应的数据，values[:,2]y轴
#对应的数据，marker表示点的形状，
plt.xlabel('年份')
plt.ylabel('生产总值（亿元)')
plt.ylim((0,225000))#设置y的范围
plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation =45)
#range()函数 类似于 np.arange 但是range的返回值是可迭代对象而不是数组可用于索引，切片，
#plt.xticks函数,规定x轴的刻度
#没有规定y轴刻度，y轴的刻度会按照已知数据自动进行划分
#plt.xticks([0,1],[2,3],rotation = 0)
#[0,1]代表x坐标轴的0和1位置，[2,3]代表0,1位置的显示lable，rotation代表lable显示的旋转角度。
'''
官方给出的例子是：
xticks( arange(5), (‘Tom’, ‘Dick’, ‘Harry’, ‘Sally’, ‘Sue’) )
用’Tom’, ‘Dick’, ‘Harry’, ‘Sally’, 'Sue’作为[0,1,2,3,4]位置显示的label。
'''
plt.title('2000-2017年各季度国民生产总值散点图')
plt.savefig('D:\python\czpython\save_2000-2017年各季度国民生产总值散点图.png')
#plt.show()

plt.figure(figsize=(8,7))#设置画布
#绘制散点图1
plt.scatter(values[:,0],values[:,3],marker = 'o',c = 'red')
#绘制散点图2
plt.scatter(values[:,0],values[:,4],marker = 'D',c = 'blue')
#绘制按点图3
plt.scatter(values[:,0],values[:,5],marker = 'v',c = 'yellow')
plt.xlabel('年份')#添加横轴标签
plt.ylabel('生产总值(亿元)')#添加纵轴标签
plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation=45)
#range的返回值是可迭代对象，可用于索引，切片
#没有规定y轴刻度，y轴的刻度会按照已知数据自动进行划分
plt.title('2000-2017年各产业各季度国民生产总值散点图')#添加图表标题
plt.legend(['第一产业','第二产业','第三产业'])#添加图例
plt.savefig('D:\python\czpython\save_2000-2017年各产业季度国民生产总值散点图.png')
plt.show()

