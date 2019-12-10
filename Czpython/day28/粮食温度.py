from sqlalchemy import create_engine
import pandas as pd
import os
import re
from pandas import DataFrame
'''
网上许多优化教程以及官方均认为，空值置为0有利于节省空间，实际上Mysql也是这么做的，在导入数值型字段时，默认将空值置为0。 
但实际中，数据本身的空值也是包含信息的，与0值并不一样。举个栗子，有一组数据：
null, null, 1, 2, 3
求均值时应该为(1+2+3)/3=2，但在默认情况下导入数据后其均值则会变为(0+0+1+2+3)/5=1.2了。两者包含的信息显然不一样。
'''

engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/testdb?charset=utf8')
temperature = pd.read_sql('2.1',con=engine)
#print(temperature)
file_name = os.listdir('C:/Users\cz1999\Desktop\data\data')
file_name.sort()
#file_name.sort(key = lambda x:str(x[:-4]))
#print(os.listdir('C:/Users\cz1999\Desktop\data\data'))

temperature['barn_name'] = '龙嘉直属库_春阳分库_砖圆03'
temperature.to_sql('2.3',con =engine,index=False,if_exists= 'replace')
#temperature['time'] = ''
#print(temperature)
s=[]
for filename in file_name:
    a = re.search('\d+-\d+-\d+\s\d+_\d+_\d+',filename).group()#使用group()函数获得匹配结果
    s.append(a)
    print(file_name)

#print(s)#字符串添加进列表时会有引号
c = {'time':s}
data = DataFrame(c)
#print(data)
lk = pd.concat([temperature,data],axis=1,join ='outer')
#print(pd.concat([temperature,data],axis=1,join ='outer'))

lk.to_sql('2.4',con=engine,index = False,if_exists='replace')

mydata1 = lk.melt(
id_vars = ["raw","layer","barn_name","time"],   #要保留的主字段
var_name = ["columns"],                   #拉长的分类变量
value_name = "temperature"                  #拉长的度量值名称
        )

print(mydata1.loc[0:20,:])
