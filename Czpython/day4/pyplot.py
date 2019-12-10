import numpy as np #引入numpy库
import matplotlib.pyplot as plt #引入matplotlib.pyplot
# %matplotlib inline 表示在行中显示图片，在命令行中运行报错
data  = np.arange(0,1.1,0.01)
plt.title('lines')#添加标题
plt.xlabel('x')#添加x轴的名称
plt.ylabel('y')#添加y轴名称
plt.xlim((0,1))#确定x轴的范围
plt.ylim((0,1))#确定y轴的范围
plt.xticks([0,0.2,0.4,0.6,0.8,1])
plt.yticks([0,0.2,0.4,0.6,0.8,1])
plt.plot(data,data**2)#添加y = x^2曲线
plt.plot(data,data**4)#添加y = x^4曲线
plt.legend(['y = x^2','y = x^4'])
plt.savefig("D:\python\czpython\y = x^2.png")
plt.show()