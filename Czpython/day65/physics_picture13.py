import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] =  'SimHei' #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #确保字符显示正常

T = [100,100,100,100,99.9,94.5,63.7,31.1,13.4,7.4,6.1,6.0,6.1,6.1,6.1,6.0]

angle = [-85,-65,-45,-30,-25,-5,0,5,25,30,45,65,85]
Ts_max = [1.1,61.5,87.8,97.4,98.7,100,100,99,96.1,94.7,84.7,59.0,6.0]
Ts_min = [7.4,16.9,12.4,10.8,10.5,9.9,9.8,10,10.7,11.3,13.4,16.9,3.7]



#子图1
#axl = plt.add_subplot(4,2,1)
#电压-透射率
plt.figure(figsize=(12,8))
plt.plot(np.arange(0,3.2,0.2),T,color = 'k',linestyle = '-',marker='o')
plt.xlabel('电压(V)')
plt.ylabel('透射率(%)')
plt.xticks(np.arange(0,3.2,0.2))
plt.ylim(0,100)
plt.yticks(range(0,110,5))
plt.grid()

for x,y in zip(np.arange(0,1.8,0.2),T):
    plt.text(x+0.08,y+0.53,y,ha='center',va='bottom',fontsize=20)
for x,y in zip(np.arange(1.8,3.2,0.2),[7.4,6.1,6.0,6.1,6.1,6.1,6.0]):
    plt.text(x+0.08,y-1.8,y,ha='center',va='top',fontsize=20)

for a,b in zip([1.04],[90]):
    plt.text(a+0.25,b-2.1,'----------阈值电压: '+str(float(a))+' V', ha='center', va='bottom', fontsize=20)
for a,b in zip([1.68],[10]):
    plt.text(a+0.25,b-2.1,'------------关断电压: ' + str(float(a))+' V', ha='center', va='bottom', fontsize=20)


plt.savefig('D:/python/czpython/save_physics.png')
plt.show()
