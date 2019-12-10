from sqlalchemy import create_engine
import pandas as pd
#创建一个MYSQL连接器，用户名为root,密码为1234
#地址为127.0.0.1,数据库名称为testdb,编码为UTF-8
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')

#使用read_sql_table读取订单详情表
#DataFrame的常用属性values(元素),index(索引),columns(列名),dtypes(类型),size(元素个数),ndim(维度数),shape(形状)
detail1 = pd.read_sql_table('meal_order_detail1',con = engine)
#index（索引）
print('使用read_sql_table读取订单详情表的长度为：',detail1.index)
#values(所有值）
print('订单详情表的所有值为：','\n',detail1.values)
#columns（列名）
print('订单详情表的列名为：','\n',detail1.columns)
#dtypes(数据类型）
print('订单详情表的数据类型为：','\n',detail1.dtypes)
#size(元素个数）
print('订单详情表的元素个数为',detail1.size)
#ndim(维度数）
print('订单详情表的维度数为',detail1.ndim)
#形状(size)
print('订单详情表的形状为',detail1.shape)
#使用T属性进行转置
print('订单表转置前的形状为',detail1.shape)
print('订单表转置后的形状为',detail1.T.shape)