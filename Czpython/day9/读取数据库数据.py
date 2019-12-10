from sqlalchemy import create_engine
import pandas as pd
#创建一个MYSQL连接器，用户名为root,密码为1234
#地址为127.0.0.1,数据库名称为testdb,编码为UTF-8
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/testdb?charset=utf8')

#使用read_sql_table、read_sql_query、read_sql函数读取数据库数据

#使用read_sql_query查看testdb中的数据表数目
formlist = pd.read_sql_query('show tables',con = engine)
print('test数据库数据表清单为：','\n',formlist)

#使用read_sql_table读取订单详情表
detail1 = pd.read_sql_table('meal_order_detail1',con = engine)
print('使用read_sql_table读取订单详情表的长度为：',len(detail1))

#使用read_sql读取订单详情表
detail2 = pd.read_sql('select * from meal_order_detail2',con = engine)
print('使用read_sql函数+sql语句读取订单详情表的长度为：',len(detail2))
detail3 = pd.read_sql('meal_order_detail3',con = engine)
print('使用read_sql函数+表格名称读取订单详情表长度为',len(detail3))