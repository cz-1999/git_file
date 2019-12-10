import numpy as np
import matplotlib.pyplot as plt

#原图
x = np.linspace(0,4*np.pi)#生成样本数默认为50,必须是非负
y = np.sin(x)#生成y轴数据
plt.plot(x,y,label="$sin(x)$")#绘制sin曲线图
plt.title('sin')
plt.savefig("D:\python\czpython\默认sin曲线.png")
#plt.show()

#修改rc参数后的图
plt.rcParams['lines.linestyle'] = '-.'
plt.rcParams['lines.linewidth'] = 3
plt.plot(x,y,label="$sin(x)$")#绘制三角函数
plt.title('sin')
plt.savefig("D:\python\czpython\修改rc参数后的sin曲线.png")
#plt.show()
'''
#无法显示中文标题
plt.plot(x,y,label="$sin(x)$")#绘制三角函数
plt.title('sin曲线')
plt.savefig("D:\python\czpython\无法显示中文标题sin曲线.png")
#plt.show()
'''
#设置rc参数显示中文标题
#设置字体为SimHei显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False #设置正常显示符号
plt.plot(x,y,label = "$sin(x)$") #绘制三角函数
plt.title("sin曲线")
plt.savefig("D:\python\czpython\显示中文标题sin曲线.png")
plt.show()