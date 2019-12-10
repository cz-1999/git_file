from sqlalchemy import create_engine
import pandas as pd
import datetime
import numpy as np
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/testdb?charset=utf8')
print(engine)

#查看P2P网络贷款数据主表的基本信息
master = pd.read_csv('D:\python\czpython/Training_Master.csv',encoding='gbk')
print(master.shape,master.ndim,master.memory_usage())
print(master.describe())

def dropNullStd(data):
    beforelen = data.shape[1] #行的宽度
    colisNull = data.describe().loc['count'] == 0  #把count==0的列，按行的形式放到colisNull中
    for i in range(len(colisNull)):
        if colisNull[i]:
            data.drop(colisNull.index[i],axis = 1,inplace = True)
    std_is_zero = data.describe().loc['std'] ==0
    for i in range(len(std_is_zero)):
        if std_is_zero[i]:
            data.drop(std_is_zero.index[i],axis = 1,inplace = True)
    afterlen = data.shape[1]
    print('删除列的数目为',beforelen-afterlen)   #函数内部定义的变量在函数外无法使用
    print('删除后数据的形状为',data.shape)
dropNullStd(master)
#提取用户信息更新表和登录信息表的时间信息
loginfo = pd.read_csv('D:/python/czpython/Training_LogInfo.csv')
userupdate = pd.read_csv('D:/python/czpython/Training_Userupdate.csv')
print(loginfo.shape)
print(userupdate.shape)
loginfo['LogInfo3'] = pd.to_datetime(loginfo['LogInfo3'])
userupdate['UserUpdateInfo2'] = pd.to_datetime(userupdate['UserupdateInfo2'])
print(loginfo['LogInfo3'].dtypes,userupdate['UserupdateInfo2'].dtypes)

year = [i.year for i in loginfo['LogInfo3']]  #year是一个列表
month = [i.month for i in loginfo['LogInfo3']]
day = [i.day for i in loginfo['LogInfo3']]
print(year[0:5],month[0:5],day[0:5])
year = [i.year for i in userupdate['UserUpdateInfo2']]
month = [i.month for i in userupdate['UserUpdateInfo2']]
day = [i.day for i in userupdate['UserUpdateInfo2']]
print(year[0:5],month[0:5],day[0:5])
timedelta=userupdate['UserUpdateInfo2']-loginfo['LogInfo3'] #转换成小时，分钟，不成功
print(timedelta)
print(datetime.datetime.now())

#使用分组聚合方法进一步分析用户信息更新表和登录信息表
detailGroup1 = loginfo[['Idx','LogInfo3']].groupby(by='Idx')
detailGroup2 = userupdate[['Idx','UserUpdateInfo2']].groupby(by='Idx')
print(detailGroup1.agg([np.min,np.max]).head())
print(detailGroup2.agg([np.min,np.max]).head())
print(detailGroup1.agg(np.size).head())
print(detailGroup2.agg(np.size).head())

#对用户信息表更新表和登录信息表进行长宽表转换
print(master.shape,userupdate.shape,loginfo.shape)

#master1 = master.pivot_table(index=['Idx'],columns=['LogInfo1','LogInfo2','LogInfo3'])

#读取mtcars数据集
mtcars = pd.read_csv('D:/python/czpython/mtcars.csv')
print(mtcars)
print(mtcars.shape,mtcars.size,'\n',mtcars.describe().iloc[0:10,0:5])
#函数是  pd.pivot_table() 而不是  mtcars.pivot_table(),函数写错了，找了半个多小时，
mtcarsPivot = pd.pivot_table(mtcars[['cyl','mpg','hp','carb']],index=['cyl','carb'])
print(mtcarsPivot)
#group函数分组
mtcarsGroup = mtcars.loc[:,['cyl','carb','mpg','hp']].groupby(by=['cyl','carb']).mean()
print(mtcarsGroup)
