#创建数据库连接
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/testdb?charset=utf8')

#读取数据
#read_sql_table不能接收sql语句，可以接收表名
detail = pd.read_sql_table('meal_order_detail1',con = engine)

#删除dataframe的某列，使用drop函数，drop函数常用4个参数,labels:接收string或array, string可以接收表名,删除某一列
#array可以接收数组,删除某一行或几行
#代表删除行和列的标签,axis:接收0或1
#代表操作轴向，默认为0，level:接收int或索引名。代表标签所在级别，默认为None，inplace:接收boolean(布尔值)代表操作是否对元数据生效
#默认为False

#删除某列
detail1 = detail.drop(labels='detail_id',axis=1)
print(detail1.columns)

#删除一行
detail2 = detail.drop(labels=0,axis=0)
print(detail2)
#删除几行
detail3 = detail.drop(labels=range(1,11),axis=0) #range函数返回的是一个可迭代对象,不是列表，但是也能接收
print(detail3)
detail4 = detail.drop(labels=[0,1,2,3],axis=0)
print(detail4)

#描述分析dataframe数据
#数值型特征的描述性统计分析，包括了计算数值型数据的完整情况，最小值，均值，最大值，中位数，四分位数，极差，标准差，方差，协方差
#和变异系数等，在numpy 库中给出了很多统计函数,np.min(),np.max(),np.mean(),pandas库基于numpy可以使用numpy库中函数
#进行计算,  np.mean(dataframe)
print(np.mean(detail['amounts']))

#求菜品售价的均值也可以通过pandas提供的函数来进行计算,dataframe.mean(),pandas也提供了numpy库中的函数，使用方式
#dataframe.函数名(),pandas还提供了一个describe函数，能够一次性得出数据框中所有数值型特征的非空值数目,均值，四分位数
#标准差
print(detail['amounts'].max())
print(detail.describe())

#类别型数据统计分析,描述类别型特征的分布状况,可以使用频数统计表，pandas中有实现频数统计的函数values_counts，对菜品销售数据
#中的菜品名(aname)进行频数统计
print(detail['dishes_name'].value_counts()[0:10]) #先进行了列索引之后进行了行索引

#pandas提供了category类型,可以使用astype函数将dataframe转换为category，describe()函数还可以支持对category
#类型的数据，进行描述性分析统计，4个统计量为列非空元素的数目,类比额的数目，数目最多的类别，和数目最多类别的数目
#格式为dataframe[] = dataframe[].astype(category)
detail['dishes_name'] = detail['dishes_name'].astype('category')
print(detail['dishes_name'].describe())

from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/testdb?charset=utf8')

detail = pd.read_sql('meal_order_detail1',con=engine)
order = pd.read_csv('D:/python/czpython/meal_order_info.csv',encoding='gbk')
user = pd.read_excel('D:/python/czpython/users.xlsx')
print(detail.ndim)

#多列菜品销量的描述性统计,先用loc函数切片再用describe函数
print(detail.loc[:,['counts','amounts']].describe())

#多列类别型数据的描述性统计，先转换数据类型为category,loc函数切片，再用describe函数描述性统计
detail['dishes_name'] = detail['dishes_name'].astype('category')
detail['order_id'] = detail['order_id'].astype('category')
print(detail.loc[:,['order_id','dishes_name']].describe())
print(detail.loc[0])
print(detail.iloc[0])
'''
#删除全为空值或所有元素取值相同的列
#通过descripe可以发现部分数据整列为空或取值相同，可以通过dataframe的增删操作，将这部分数据去掉
#定义一个函数,格式     def 函数名(参数):

print(detail.describe())
#colisNull = detail.describe().loc['count'] == 0
#print(colisNull)
def dropNullStd(data):
    beforelen = data.shape[1] #列的宽度
    colisNull = data.descripe().loc['count'] == 0     #切片出一行数据
    for i in range(len(colisNull)):
        if colisNull[i]:
            data.drop(colisNull[i],axis=1,inplace = True)
'''

#转换与处理时间序列数据
#数据分析对象包括了数值型，类别型，时间类型，通过时间类型的数据可以获取到对应的年月日星期等信息，但是时间类型数据在读入
#python后常以字符串的形式出现,无法实现大部分与时间相关的分析，pandas库继承了numpy库的datetime64以及timedelta64模块，
#能够实现能够实现字符串的转换，信息提取和时间运算

#转换字符串时间为标准时间
#Timestamp是时间类中最基础的，也是最为常用的,通常将与时间相关的字符串转换成Timestamp pandas提供了 to_datetime函数
#可以将字符串时间转化成Timestamp, to_date_time函数的用法,  dataframe = pd.to_date_time(dataframe)

order = pd.read_csv('D:/python/czpython/meal_order_info.csv',encoding='gbk')
print('\n',order['lock_time'].dtypes)
order['lock_time'] = pd.to_datetime(order['lock_time'])
print(order['lock_time'].dtypes)

#Timestamp类型的时间是有限制的
print(pd.Timestamp.min)
print(pd.Timestamp.max)

#除了将数据从原始dataframe中直接转化为Timestamp格式外，还可以将数据单独提取出来，将时间数据转换成DatetimeIndex
# 和PeriodIndex格式，但是不能直接转
#将时间数据转换成DatetimeIndex和PeriodIndex格式，转换的函数也为pd.DatetimeIndex(),pd.PeriodIndex()
#转换成PeriodIndex时,需要通过freq参数指定时间间隔，常用的时间间隔为Y(年),M(月),D(日),H(时),T(分),S(秒),
#freq可以用来调整数据的精确度， 两个函数可以用来转换数据
#也可以用来创建时间序列数据（一列时间数据），参数非常类似 变量 = pd.DatetimeIndex(dataframe)
# 变量 = PeriodIndex(dataframe,frep = '时间间隔')
DatetimeIndex = pd.DatetimeIndex(order['lock_time'])
PeriodIndex = pd.PeriodIndex(order['lock_time'],freq='S')
print(PeriodIndex[0:1])
print(DatetimeIndex[0:1])

#DatetimeIndex是用来指代一系列时间点的数据结构，PeriodIndex是用来指代一系列时间段的数据结构

#提取时间序列数据信息,在多数涉及与时间相关的数据处理，统计分析过程中，都需要提取时间中的年份月份等数据，使用对应的Timestamp
#类属性可以查看，Timestamp.属性，
#对dataframe中某一列时间信息数据的提取,以列表的形式存放
year = [i.year for i in order['lock_time']]
month = [i.month for i in order['lock_time']]
day = [i.day for i in order['lock_time']]
weekday = [i.weekday_name for i in order['lock_time'] ]
print(year[0:5],month[0:5],day[0:5],weekday[0:5])

#在DatetimeIndex和PeriodIndex中提取对应信息，直接使用类属性
#PeriodIndex相比DateimeIndex少了weekday_name属性，可以通过提取weekday属性，而后对0-6这7个标签分别赋值为Monday-Sunday
print(DatetimeIndex.weekday_name[:5])
print(PeriodIndex.weekday[:5])

#加减时间数据,pandas中的时间数据和现实生活中的时间数据一样可以做运算,要用到pandas的Timedelta类
#Timedelta是时间相关类中的一个异类，不仅能够使用正数表示时间，还能够使用负数例如1s,2min,3h等，配合常规时间类能够轻松实现时间的算术运算
#Timedelta时间周期中没有年和月

#加运算，将lock_time数据向后平移一天
print(order['lock_time'].head())
timel = order['lock_time'] + pd.Timedelta(days=1)
print(timel.head())

'''
#时间序列和Timestamp类不能直接相加，可以直接相减，得出一个Timedleta类
timel2 = order['lock_time'] + pd.to_datetime('2017-1-1') #时间字符串要放到''内
print(timel2.head())
'''

#减运算，两个时间序列相减得出一个Timedleta类
timedleta = order['lock_time'] - pd.to_datetime('2017-1-1 20:33:40')
print(timedleta)
print(pd.to_datetime('2017-1-1 20:33:40').hour)
print(timedleta.dtypes)

#任务实现
#时间字符串转换为标准时间格式
import pandas as pd
order = pd.read_csv('D:/python/czpython/meal_order_info.csv',encoding='gbk')
order['use_start_time'] = pd.to_datetime(order['use_start_time'])
order['lock_time'] = pd.to_datetime(order['lock_time'])

#提取菜品信息表中的年月日和星期信息
year1 = [i.year for i in order['use_start_time']]
month1 = [i.month for i in order['lock_time']]
day1 = [i.day for i in order['lock_time']]
dayofyear1 = [i.dayofyear for i in order['lock_time']]
print(dayofyear1[0:5])

#查看订单信息表使劲按统计信息
timemin = order['lock_time'].min()
timemax = order['lock_time'].max()
timedleta =timemax - timemin
print(timemin)
print(timemax);print(timedleta)

#Timedleta类也可以使用函数
checkTime = order['lock_time'] - order['use_start_time']
print(checkTime.mean())
print(checkTime.min())
print(checkTime.max())
#通过数据发现最短时间和最长时间均为异常值，开始时间不可能在结算时间之后,最短时间为负数，点餐时间不可能持续16天


