from sqlalchemy import create_engine
import pandas as pd
#创建一个MYSQL连接器，用户名为root,密码为1234
#地址为127.0.0.1,数据库名称为testdb,编码为UTF-8
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')

#使用read_sql_table读取订单详情表
detail1 = pd.read_sql_table('meal_order_detail1',con = engine)
print('使用read_sql_table读取订单详情表的长度为：',len(detail1))#行数

#loc内部传入表达式
#loc内部还可以传入表达式，结果会返回满足表达式的所有值
print('detail1中order_id为458的dishes_name为: \n',detail1.loc[detail1['order_id']=='458',['order_id','dishes_name']])
#此处iloc方法不能接收表达式，原因在于，此处条件返回的为一个布尔值的Series,而iloc可以接收的数据类型并不包括Series
#根据Series的构成只要请问取出Series的values就可以了
#print('detail1中order_id为458的第1、5列数据为: \n',detail1.iloc[detail1['order_id']=='458',[1,5]])

#使用iloc实现条件切片
print('detail1中order_id为458的第1、5列数据为: \n',detail1.iloc[(detail1['order_id']=='458').values,[1,5]])

#切片方法ix
#ix方法更像是loc和iloc两种切片的融合。ix方法在使用的时候即可接收索引名称，也可以接收索引位置。
#使用方法为DataFrame.ix[行索引名称或位置或条件,列索引名称或位置]

#使用ix时需要注意，当索引名称和位置不重叠时，ix则根据名称或位置识别,
#当索引名称和位置部分重叠时，ix默认优先识别名称
#当索引名称和位置重叠时，ix按行名称，均为闭区间。
print('列名为dish_name行名为2,3,4,5,6的数据为: \n',detail1.loc[2:6,'dishes_name'])
print('列位置为5,行位置为2,3,4,5,6的数据为: \n',detail1.iloc[2:6,5])
#print('列位置为5,行名为2,3,4,5,6的数据为: \n',detail1.ix[2:6,5])#会报错，ix方法过时了
