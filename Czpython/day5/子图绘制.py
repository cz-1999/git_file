import numpy as np
import matplotlib.pyplot as plt
rad = np.arange(0,np.pi*2,0.01)
#第一幅子图
pl = plt.figure(figsize=(8,6),dpi = 80)#确定画布大小
axl = pl.add_subplot(2,1,1)#创建一个二行一列的子图，并开始绘制第一幅图
plt.title('lines')#添加标题
plt.xlabel('x')#添加x轴名称
plt.ylabel('y')#添加y轴名称
plt.xlim((0,1))#确定x轴的范围
plt.ylim((0,1))#确定y轴的范围
plt.xticks([0,0.2,0.4,0.6,0.8,1])#规定x轴刻度
plt.yticks([0,0.2,0.4,0.6,0.8,1])#规定y轴刻度
plt.plot(rad,rad**2)#添加y = x^2曲线
plt.plot(rad,rad**4)#添加y = x^4曲线
plt.legend(['y= x^2','y=x^4'])#添加标签
#第二幅子图
ax2 = pl.add_subplot(2,1,2)#开始绘制第二幅
plt.title('sin/cos')#添加标题
plt.xlabel('rad')#添加x轴的名称
plt.ylabel('value')#添加y轴名称
plt.xlim((0,np.pi*2))#确定x轴的范围
plt.ylim((-1,1))#确定y轴的范围
plt.xticks([0,np.pi/2,np.pi,np.pi*1.5,np.pi*2])#规定x轴刻度
plt.yticks([-1,-0.5,0,0.5,1])#确定y轴刻度
plt.plot(rad,np.sin(rad))#添加sin曲线
plt.plot(rad,np.cos(rad))#添加cos曲线
plt.legend(['sin','cos'])#添加标签
plt.savefig("D:\python\czpython\sincos.png")
plt.show()