import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] =  'SimHei' #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #确保字符显示正常


V1=[13.3,26.5,39.6,52.7,65.8,79.0,92.3,105.3,118.5,131.7,
    13.2,26.3,39.3,52.6,66.0,79.5,92.7,105.9,119.0,131.8,
    66.9,93.3,124.2,130.4,131.5,131.9,132.3,132.3,132.3,132.4,132.3,130.9,91.5,61.9,50.6]

V2=[13.5,26.8,40.1,53.5,66.7,80.0,93.4,106.5,119.7,132.9,
    13.5,26.8,40.0,53.3,66.7,80.1,93.3,106.7,119.7,132.5,
    67.3,94.3,125.2,131.4,132.5,132.9,133.2,133.3,133.2,133.3,133.3,131.8,92.4,62.8,51.5]

V3=[13.5,26.9,40.1,53.5,66.7,80.0,93.4,106.4,119.6,132.8,
    13.5,26.9,40.0,53.3,66.7,80.1,93.3,106.6,119.7,132.5,
    67.3,94.3,125.2,131.3,132.4,132.8,133.2,133.2,133.2,133.2,133.3,131.8,92.4,62.8,51.5]

V4=[13.2,26.5,39.5,52.7,65.8,79.0,92.3,105.3,118.6,131.8,
    13.0,26.3,39.3,52.7,66.1,79.5,92.8,106.0,119.1,131.9,
    66.3,93.3,124.3,130.4,131.5,131.9,132.2,132.3,132.3,132.3,132.3,130.9,91.4,61.9,50.6]

#子图1
VH1 = []
#子图2
VH2 = []
#子图3
B = []
VH=[]

VH3 = []
x=[0,2,4,6,8,10,15,20,25,30,35,40,45,48,50]

for i,j,k,l in zip(V1,V2,V3,V4):
    VH.append(round((np.fabs(float(i))+np.fabs(float(j))+np.fabs(float(k))+np.fabs(float(k)))/4,1))

print("\n")
for i in range(0,10):
    VH1.append(VH[i])
    print(VH[i])

print("\n")
for i in range(10,20):
    VH2.append(VH[i])
    print(VH[i])

print("\n")
for i in range(20,35):
    VH3.append(VH[i])
    print(VH[i])

print("\n")
for i in range(0,35):
    print(VH[i])

print("\n")
for i in VH3:
    print(round(i/(169.7*5)*1000,1))
    B.append(round(i/(169.7*5)*1000,1))

pl = plt.figure(figsize=(10,12),dpi=100) #设置画布

#子图1
#VH-IS 曲线

axl = pl.add_subplot(3,1,1)
plt.plot(range(1,11),VH1,color = 'k',linestyle = '-')
plt.xlabel('工作电流IS(mA)')
plt.ylabel('霍尔电压VH(mV)')
plt.xticks(range(1,11))
plt.ylim(0,140)
plt.yticks(range(0,140,10))
plt.grid()

#子图2
#VH-IM曲线
axl2 = pl.add_subplot(3,1,2)
plt.plot(range(100,1100,100),VH2,color = 'k',linestyle = '-')
plt.xlabel('工作电流IM（mA）')
plt.ylabel('霍尔电压VH(mV)')
plt.xticks(range(100,1100,100))
plt.ylim(0,140)
plt.yticks(range(0,140,10))
plt.grid()


#子图3
#B-x曲线

axl3 = pl.add_subplot(3,1,3)
plt.plot(x,B,color = 'k',linestyle = '-')
plt.xlabel('距离x(mm)')
plt.ylabel('磁场强度B(mT)')
plt.xticks(range(0,52,2))
plt.ylim(0,180)
plt.yticks(range(0,180,20))
plt.grid()


plt.savefig('D:/python/czpython/save_physics8.png')
plt.show()

