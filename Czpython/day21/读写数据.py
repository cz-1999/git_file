
#读取不同数据源的数据
#不同的数据源需要使用不同的函数读取，常见的数据源有三种，分别是数据库文件，文本文件，Excel文件

#读取数据库文件之前，要建立与Mysql的连接

from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/testdb?charset=utf8')
#在create_engine中输入的是一个 连接字符串 ,在使用python的sqlalchemy时,mysql和oracle数据库连接字符串格式如下
#数据库名+连接工具名://用户名:密码@数据库IP地址:数据库端口号/数据库名称?charset = 数据库数据编码
print(engine)

#读取数据库文件

#实现数据库读取的三个函数,pd.read_sql, pd.read_sql_query, pd.read_sql_table
#pd.read_sql_query函数只能实现查询操作，可以查询数据库中的信息，例如表，不能直接读取数据中的某个表，
# pd.read_sql_table只能实现读取表不能实现查询， pd.read_sql两者都可以，3个函数的参数几乎一致,常用的2个参数为
#sql or tabel_name : 接收string，表示读取的数据的表名或者sql语句  con : 接收数据库连接,表示数据库连接信息

import pandas as pd
#不能把表读入内存，可以查询数据库中的信息   read_sql_query+sql语句
formlist = pd.read_sql_query('show tables',con = engine)#show tables 展示数据库中表的信息
print(formlist)
#可以把表读入内存 并以dataframe的形式存储下来，保存到一个变量内，不能对数据库进行查询操作
detail1 = pd.read_sql_table('meal_order_detail1',con =engine)
print('\n',len(detail1))
#可以把表读入内存，也能直接对数据库进行查询操作    read_sql + 表名
detail2 =pd.read_sql('meal_order_detail2',con = engine)
print(len(detail2))
#read_sql + sql语句
detail3 = pd.read_sql('select * from meal_order_detail2',con = engine)
print(len(detail3))

#使用to_sql的方法写入数据,往数据库中新添加一个表，需要先读取出一个表,然后使用 to_sql 函数,一般常用到4个参数
#name:接收string，代表数据库表名，con:接收数据库连接 ，index:接收True和False,表示是否将行索引作为数据传入数据库,
#默认为True, if_exists: 接收fail,replace,append ,fail表示，如果存在则不执行操作，replace表示如果存在，则替换，
# append表示在原始数据库表的基础上追加数据

detail1.to_sql('test2',con = engine,index=False,if_exists='replace')
formlist1 = pd.read_sql_query('show tables',con = engine)

#读取文本文件
#两个函数read_table，read_csv,参数多数相同，常用4个参数，filepath:文件路径,sep:文件分割符,header:接收int或sequence
#表示将某行或多行数据作为列名,默认为infer表示自动识别，encoding:表示编码格式

order = pd.read_table('D:/python/czpython/meal_order_info.csv',sep=',',encoding ='gbk' )
print(len(order))
order1 = pd.read_csv('D:/python/czpython/meal_order_info.csv',encoding='gbk')
print(len(order1))

order2 = pd.read_table('D:/python/czpython/meal_order_info.csv',sep =';',encoding='gbk')
print(order2)

order3 = pd.read_csv('D:/python/czpython/meal_order_info.csv',sep =',',header=None,encoding='gbk')
print(order3)
#编码格式错误会报错
#order4 = pd.read_csv('D；/python/czpython/meal_order_info.csv',sep = ',',encoding='utf8')
#print(order4)


import os
#写入文本文件
#利用to_csv函数将内存中的dataframe形式的数据写入csv文件，常用3个参数,path_or_buf:写入路径,sep:分隔符
# index；是否将行索引写入文件，默认为True
order.drop(labels='emp_id',axis=1,inplace=True)

#保存的文件名称相同会覆盖掉原文件
order.to_csv('D:/python/czpython/orderInfo123.csv',sep=',',index=False)

print(os.listdir('D:/python/czpython/'))
#将dataframe形式的数据以csv的格式存起来后,在进行读取，编码格式要换成 utf8
order4 = pd.read_csv('D:/python/czpython/orderInfo123.csv',sep=',',encoding='utf8')
print(order4)

#读取Excel文件,pd.read_excel函数读取 xls,xlsx两种格式的Excel文件,常用2个参数 io:接收string,表示文件路径,
# sheetname: 接收int 或 string,代表Excel表内数据的分表位置，默认为0,例如sheet1,sheet2

#读取Excel文件以DataFrame的形式存储到内存中
user = pd.read_excel('D:/python/czpython/users.xlsx')
print(len(user))

#Excel文件的存储
#to_excel函数和to_csv函数常用参数一致,区别之处在于

# sheet_name可以修改分表的名字
user.to_excel('D:/python/czpython/userInfo.xlsx',sheet_name='cz')#文件类型要写，不然会报错

#任务实现

#读取数据库数据,读取数据的表名或sql语句
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/testdb?charset=utf8')
order1 = pd.read_sql_table('meal_order_detail1',con = engine)
print(len(order1))
order2 = pd.read_sql_table('meal_order_detail2',con = engine)
print(len(order2))
order3 = pd.read_sql_table('meal_order_detail3',con = engine)
print(len(order3))

#读取csv数据，数据的存储路径
orderInfo = pd.read_csv('D:/python/czpython/orderInfo.csv',sep=',',encoding='utf8')
print(len(orderInfo))

#读取Excel数据，数据的存储路径
userInfo = pd.read_excel('D:/python/czpython/userInfo.xlsx',sheet_name='cz')
print(len(userInfo))




