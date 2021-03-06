import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] =  'SimHei' #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #确保字符显示正常

#1
I0 = [84,176,270,364,460,556,651,745,834,932]
If = [87,181,278,375,472,570,668,765,862,957]

#2
V =  [45,94,145,196,246,297,347,397,446,496]

#3
V2 = [495,714,847,936,1000,1048,1085,1115,1140,1160]

#4
HZ = [1,5,9,20,30,50,120,150,190]
V3 = [220,851,901,950,950,900,750,700,600]

#5
L_out = [111,287,480,681,888,1098,1311,1524]

#6
HZ2 =[1,5,9,100,500,800,1500,2500,3500,4500,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]
V4 = [1700,4800,5000,6000,6100,6100,6000,5900,5600,5400,4600,4400,4200,4100,4005,4000,3950,3900,3850,3800]

#7
V5 = [0.9,2.4,4.5,5.9,7.7,10,11.5]#最大不失真电压
V6 = [0.26,0.82,1.66,2.35,3.34,4.26,4.62]#峰值电压


pl = plt.figure(figsize=(20,18),dpi=100) #设置画布

#子图1
axl = pl.add_subplot(4,2,1)
#零偏绘图
plt.plot(range(1,11),I0,color = 'k',linestyle = '-')
#负偏绘图
plt.plot(range(1,11),If,color = 'k',linestyle = '-')

plt.xlabel('驱动电流（mA）')
plt.ylabel('光生电流(亮度)')
plt.xticks(range(1,11))
plt.ylim(0,1000)
plt.yticks(range(0,1200,100))
plt.grid()

#子图2
axl2 = pl.add_subplot(4,2,2)
plt.plot(range(1,11),V,color = 'k',linestyle = '-')
plt.xlabel('驱动电流（mA）')
plt.ylabel('光生电压')
plt.xticks(range(1,11))
plt.ylim(0,500)
plt.yticks(range(0,500,50))
plt.grid()

#子图3
axl3 = pl.add_subplot(4,2,3)

plt.plot(range(10,110,10),V,color = 'k',linestyle = '-')
plt.xlabel('驱动电流（mA）')
plt.ylabel('光生电压')
plt.xticks(range(10,110,10))
plt.ylim(0,1200)
plt.yticks(range(0,1400,200))
plt.grid()

#子图4
axl4 = pl.add_subplot(4,2,4)
plt.plot(HZ,V3,color = 'k',linestyle = '-')
plt.xlabel('驱动电流频率(HZ)')
plt.ylabel('光生电压(mV)')
plt.xticks(HZ)
plt.ylim(0,1000)
plt.yticks(range(0,1000,100))
plt.grid()

#子图5
axl5 = pl.add_subplot(4,2,5)
plt.plot(range(200,1800,200),L_out,color = 'k',linestyle = '-')
plt.xlabel('输入')
plt.ylabel('输出')
plt.xticks(range(200,1800,200))
plt.ylim(0,1600)
plt.yticks(range(100,1800,200))
plt.grid()

#子图6
axl6 = pl.add_subplot(4,2,6)
plt.plot(HZ2,V4,color = 'k',linestyle = '-')
plt.xlabel('频率(Hz)')
plt.ylabel('输出电压(mV)')
plt.xticks(HZ2)
plt.ylim(0,7000)
plt.yticks(range(1000,7000,500))
plt.grid()

#子图7
axl7 = pl.add_subplot(4,2,7)
plt.plot(range(1,8,1),V5,color = 'k',linestyle = '-')
plt.plot(range(1,8,1),V6,color = 'k',linestyle = '-')
plt.xlabel('偏置电流(mA)')
plt.ylabel('电压(V)')
plt.xticks(range(1,8,1))
plt.ylim(0,12)
plt.yticks(range(1,13,1))
plt.grid()

plt.savefig('D:/python/czpython/save_physics.png')
plt.show()