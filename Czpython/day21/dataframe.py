#dataframe是最常用的pandas对象，类似于Excel表格,相当于内存中的数据库
#dataframe的常用属性有 values(元素),index(索引),columns(列名),dtypes(类型),
#size(元素个数),ndim(维度),shape(数据形状)

#index(索引)一般是指行索引，列索引一般是列名

#创建数据库连接
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/testdb?charset=utf8')

#读取数据
#read_sql_table不能接收sql语句，可以接收表名
detail = pd.read_sql_table('meal_order_detail1',con = engine)
#dataframe的索引
print(detail.index)
#元素(值)
print(detail.values)
#列名
print(detail.columns)
#类型
print(detail.dtypes)
#大小
print(detail.size)
#维度
print(detail.ndim)
#形状
print(detail.shape)

#T属性能够实现dataframe的行列转置,在某些特殊场景下,某些函数方法只能作用于列或者行
# 可以使用dataframe的T属性进行转置  dataframe.T.shape

#行列转置后的形状
print(detail.T)

detail1 = detail.T
#提取某一行数据,转置一下提取这一列的数据，####不行
print(detail1)
print(detail['counts'])

#查改增删DataFrame数据

#使用字典访问key值(列名)的方式访问单列数据, dataframe['columns'], 之后再访问行数据,以一维数组索引的方式
# dataframe['columns'][:]  顾头不顾尾
# 访问不是切片,只是查看

#单列数据访问
print(detail['order_id'][:])
#可以这样简写
print(detail['order_id'])

#单行数据访问
print(detail[:][0:1])

#单列多行数据访问
print(detail['order_id'][0:3])

#多列多行数据访问，列名要以列表的形式来存,中间用,隔开
print(detail[['order_id','dishes_name']][0:4])

#多行数据访问，行索引时，两个数字之间要用:隔开
print(detail[:][4:6])

#单个元素（值）访问
print(detail['order_id'][0:1])

#rows : 行  ,columns : 列

#dataframe提供了head() ,tail()方法获取多行数据
#但是这两种方法获得的数据都是从开始或末尾获取的连续数据
#默认获取前5行数据，往()中输入访问行数，即可实现目标行数的查看

print(detail.head(1))
print(detail.tail(1))

#dataframe的loc,iloc,ix的访问方式，loc, iloc,ix函数可以实现对dataframe数据的切片提取，然后进行访问
#loc是针对dataframe索引名称的切片方法，如果传入的不是索引名称，则无法切片，利用loc方法可以实现所有单层索引的切片
#dataframe.loc[行索引名称或条件,列索引名称]
#iloc与loc的区别是iloc接收的必须是行索引和列索引位置 dataframe.iloc[行索引位置，列索引位置]
#ix像是两种方法的融合,ix在使用是既可以接收索引名称也可以接收索引位置
#dataframe.ix[行索引名称或位置或条件,列索引名称或条件]


#单列切片，行和行后面的,不能省略
#.loc[]函数
dishes_name1 = detail.loc[:,'dishes_name']
print(dishes_name1)
#.iloc[]函数
dishes_name2 = detail.iloc[:,5]
print(dishes_name2)

#单行切片
#loc函数,列和列前面的,可以直接省略
print(detail.loc[0])
#iloc函数，单行切片，列和列前面的,也可以省略
print(detail.iloc[0])


#多列切片,列名以列表的形式存放，用,隔开
#.loc[]
dishes_name3 = detail.loc[:,['order_id','dishes_name']]
print(dishes_name3)
#.iloc[]
dishes_name4 = detail.iloc[:,[1,5]]
print(dishes_name4)

#使用loc 和 iloc方法取出单层索引的dataframe中的任意数据

#单行多列数据
#.loc[]
dishes_name5 = detail.loc[3,['order_id','dishes_name']]
print(dishes_name5)
#.iloc[]
dishes_name6 = detail.iloc[3,[1,5]]
print(dishes_name6)

#多行多列数据
#.loc[]
dishes_name7 = detail.loc[2:6,['order_id','dishes_name']]
print(dishes_name7)
#.iloc[]
dishes_name8 = detail.iloc[2:6,[0,5]]
print(dishes_name8)

#在使用loc方法时内部传入的行索引为一个区间时,则前后均为闭区间，而在使用iloc方法时，行索引为一个区间时，则为前闭后开区间
#loc方法和iloc方法的列索引也能作为一个区间，与行索引类似，loc的列索引去间前后均为闭区间，索引的端点值为名称
# iloc的列索引区间为前闭后开区间
dishes_name9 = detail.loc[:,'order_id':'dishes_name']
print(dishes_name9)
dishes_name10 = detail.iloc[:,1:5]
print(dishes_name10)

#loc和iloc方法的行索引和列索引不为区间时，单个数据可以直接写，多个数据要用列表的形式传入，里面的数据用,隔开，行索引与列索引之间要用,
#隔开
dishes_name11 = detail.loc[[2,3,4],'order_id':'dishes_name']
print(dishes_name11)
#可以切片出相同的行和列
dishes_name12 = detail.iloc[[2,2,4],[0,2,2]]
print(dishes_name12)

#条件切片
#loc内部可以传入表达式，结果会返回满足表达式的所有值，返回值是一个布尔值Series，iloc内部不能接收表达式，iloc可以接收的数据类
#型并不包括Series，可以取出Series的values即可

#loc内部传入表达式,表达式一般是找出,列中满足某一条件的行，行中满足某一条件的列不行
dishes_name13 = detail.loc[detail['dishes_name']=='白饭/大碗',:]
print(dishes_name13)
#iloc不能直接接收表达式,要提取出表达式返回值的values,即  (表达式).values
dishes_name14 = detail.iloc[(detail['order_id']=='458').values,[1,5]]
print(dishes_name14)

#dataframe.ix[]
#使用ix时需要注意当索引名称与索引位置部分重叠时，ix优先识别名称,即按loc函数两边均为闭区间来计算
#在使用ix函数时尽量保持行索引名称和行索引位置重叠，这样区间的两边一律按闭区间计算
print(detail.loc[2:6,'dishes_name'])
print(detail.iloc[2:6,5])
print(detail.ix[2:6,5])

#更改dataframe中的数据
#备份数据
detail.to_sql('meal_order_detail1_copy',con = engine,index=False,if_exists='replace')

#更改数据的原理是将这一部分的数据提取出来，重新赋值为新的数据，直接对原数据的更改，操作无法撤销
#将order_id为458的变换为45800
detail.loc[detail['order_id']=='458','order_id'] = '45800'
print(detail.loc[detail['order_id']=='45800','order_id'])

#为dataframe增添一列，只需要新建一个列索引，并对该索引下的数据进行赋值即可
detail['payment'] = detail['counts']*detail['amounts']
print(detail.head())
#如果新增一列的值是相同的,直接为其赋值一个常量即可
detail['cz'] = '1999'
print(detail.head())

