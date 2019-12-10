import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei' #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #保证字符正常显示
data = np.load('D:\python\czpython\国民经济核算季度数据.npz') #读入数据
name = data['columns'] #提取columns数组，视为数据的标签
values = data['values'] #提取values数组，视为数据存在的位置）

plt.figure(figsize = (6,6)) #将画布设定为正方形，则绘制的饼图是正圆
label = ['第一产业','第二产业','第三产业'] #定义饼图的标签，标签的列表
explode = [0.01,0.01,0.01] #设定各项距离距离圆心n各半径
plt.pie(values[-1,3:6],explode = explode,labels = label,autopct='%1.1f%%')#绘制饼图
#autopct ='%1.1f%%'  100.0%  小数点前面的数据对产生结果没有任何影响，小数点后面的数据表示保留小数到后几位
#autopct = '%1.2f%%'  100.00%

plt.title('2017年第一季度各产业生产总值饼图')
plt.savefig('D:\python\czpython\save_2017年第一季度各产业生产总值饼图.png')
plt.show()
