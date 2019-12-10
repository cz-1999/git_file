import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] =  'SimHei' #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #确保字符显示正常

w = [20]
for i in range(50,300,50):
    w.append(i)
print(w)
U1=[0.7,1.7,3.4,4.9,6.6,8.3]
U2=[1.3,3.3,6.9,10.6,14.1,17.9]
U3=[0.1,0.2,0.5,0.6,1.3,1.5]



#重量-电压
plt.figure(figsize=(12,8),dpi=100)
plt.plot(w,U1,color = 'k',linestyle = '-',marker='o')
plt.plot(w,U2,color = 'r',linestyle = '--',marker='o')
plt.plot(w,U3,color = 'g',linestyle = ':',marker='o')


plt.title('U - W 特性曲线')
plt.xlabel('重量(g)')
plt.ylabel('电压(mV)')

plt.xticks(w)#设置x轴标签
plt.ylim(0,20)#设置y轴范围，自动设定y轴标签

font1={'size':23} #设置图例尺寸大小
plt.legend(['单臂电桥电压','半桥电压','全桥电压'],loc='upper left',prop=font1)
plt.grid()#设置网格线

plt.savefig('D:/python/czpython/save_physics.png')
plt.show()
