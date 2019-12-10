from sqlalchemy import create_engine
import pandas as pd
#创建一个MYSQL连接器，用户名为root,密码为1234
#地址为127.0.0.1,数据库名称为testdb,编码为UTF-8
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')

#使用read_sql_table读取订单详情表
detail1 = pd.read_sql_table('meal_order_detail1',con = engine)
print('使用read_sql_table读取订单详情表的长度为：',len(detail1))#行数

#使用字典访问的内部数据的方式询问DataFrame单列数据
#使用字典访问的方式取出orderInfo中的某一列
order_id = detail1['order_id']
print('订单详情表中的order_id的形状为:',order_id.shape)

#使用访问属性的方式访问DataFrame单列数据
#使用访问属性的方式取出orderInfo中菜品名称列
dishes_name = detail1.dishes_name
print('订单详情表中的dishes_name的形状为：',dishes_name.shape)

#DataFrame单列多行数据获取
dishes_name5 = detail1['dishes_name'][:5]
#DataFrame的一列数据可以看作一个Series,访问Series基本和访问一个一维的ndarray相同
#Series可以看成另一种pandas提供的类。
print('订单详情表中的dishes_name前5各元素为：','\n',dishes_name5)

#访问DataFrame的多行多列数据
orderDish = detail1[['order_id','dishes_name']][:5]#将多个列索引名放到一个列表中去有两个[]
print(orderDish)

#访问DataFrame的某几行数据
order5 = detail1[:][1:6]
#选择所有列 用:代替
print('订单详情表的1~6行元素为：','\n',order5)

#使用DataFrame提供的head和tail函数得到多行数据
#使用者两种方法的到数据都是从开始或者末尾获取的连续数据

print('订单详情表中前5行数据为：','\n',detail1.head())
print('订单详情表中后5行数据为：','\n',detail1.tail())
print('订单详情表中后6行数据为：','\n',detail1.tail(6))
#head和tail使用的都是默认参数，所以访问的是前后5行，可以在()内输入访问行数

#DataFrame的loc、iloc访问方式
#loc的使用方法

#单列切片
dishes_name1 = detail1.loc[:,'dishes_name']
print('使用loc提取dishes_name列的size为:',dishes_name1.size)

dishes_name2 = detail1.iloc[:,3]
print('使用iloc提取第3列的size为:',dishes_name2.size)

#多列切片
orderDish1 = detail1.loc[:,['order_id','dishes_name']]
print('使用loc提取order_id和dishes_name列的size为:',orderDish1.size)

orderDish2 = detail1.iloc[:,[1,3]]
print('使用iloc提取第1列和第3列的size为:',orderDish2.size)

#花式切片
print('列名为order_id和dishes_name的行名为3的数据 \n',detail1.loc[3,['order_id','dishes_name']])
print('列名为order_id和dishes_name行名为2,3,4,5,6的数据为 \n',detail1.loc[2:7,['order_id','dishes_name']])
print('列位置为1和3，行位置为3的数据为：\n',detail1.iloc[3,[1,3]])
print('列位置为1和3，行位置为2,3,4,5,6的数据为：\n',detail1.iloc[2:7,[1,3]])

#在使用loc方法的时候如果内部传入的行索引名称权威一区间，则前后均为闭区间；在使用iloc方法时，如果内部传入的行索引
#位置或列索引位置为区间，则为前闭后开区间


