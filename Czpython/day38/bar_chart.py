from sqlalchemy import create_engine
from day35 import tablename
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#设置rc参数显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'  #设置字体为 SimHei 显示中文
plt.rcParams['axes.unicode_minus'] = False  #设置正常显示符号

engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/barn?charset=utf8')


#建立仓库内的不同温度点的数量分布柱状图，先确定温度区间，以及间隔，分成几组，统计每个区间点的数量画图柱状图，之前有个获取表名的函数，写一个循环

def tem(num):
    for table_name in tablename.fetch_tablene()[1]: #自定义函数tablename.fetch_tablene()获取表名，for循环每一个分表的表名
        table_name1= table_name  #得到不带''的表名
        table_name = '{}'.format(table_name) #format语句将{}换成tablename , 得到带 '' 的表名
        data = pd.read_sql(table_name,con=engine) #将分表读入内存
        data = np.around(np.array(list(data['temperature']))) #提取'temperature'列，np.around()函数用于四舍五入
        # 建立两个空列表
        s=[] #存不同温度区间点的数量
        label=[] #存x轴上的标签
        temperature = np.around(np.linspace(data.min(),data.max(),num+1))#用温度的最小值与最大值作为上下界，用np.linspace()函数生成 间隔相等的温度刻度值列表
        j=1
        arr = np.ones((len(data),1)) #np.ones函数建立与data行数相同的二维数组,len(data)行，1列，用于布尔值索引
        for i in temperature:
            if(i != temperature[-1]): #循环到列表的最后一个值时结束
                t = (data >= i)&(data < temperature[j]) #得到满足区间条件的布尔值，返回值是由布尔值索引组成的列表，符合的是True,不符合的是False 类似于[ True, True, False]
                l = '{}=<t<{}'.format(i,temperature[j]) #获得分组的标签
                print(np.sum(arr[t,0]))  # 用布尔值索引arr数组,如果布尔值是True,就索引相应行的第0列，求和所有满足分组条件的点的个数
                s.append(np.sum(arr[t,0])) #将不同温度区间点的数量存入列表
                label.append(l) #将标签存入列表
                j+=1
        plt.figure(figsize=(18,7)) #绘制画布
        plt.bar(range(num),s,width=0.5) #传入x轴,y轴上的数据
        plt.xlabel('温度')
        plt.ylabel('数量')
        plt.xticks(range(num),label) #x轴的标签
        plt.title(table_name)
        sql = '''D:/python/czpython/save_{}.png'''.format(table_name1) #format函数将不同的表名替换到sql里面
        plt.savefig(sql) #将所有不同表名的表存起来
        plt.show()

if __name__ == '__main__':
    #内容为空的表画不出来，最后3个表内容为空
    print('绘制所有仓库内点的温度分布柱状图')
    num = int(input('请输入分成的组数',))
    tem(num)

