from sqlalchemy import create_engine
import pandas as pd
#创建一个MYSQL连接器，用户名为root,密码为1234
#地址为127.0.0.1,数据库名称为testdb,编码为UTF-8
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')

#使用read_sql_table读取订单详情表
detail1 = pd.read_sql_table('meal_order_detail1',con = engine)
print('使用read_sql_table读取订单详情表的长度为：',len(detail1))#行数


#使用to_sql方法写入数据
#使用to_sql存储orderData
detail1.to_sql('test1',con = engine,index = False,if_exists = 'replace')
#使用read_sql读取表
formlist1 = pd.read_sql_query('show tables',con = engine)
print('新增一个表格后，testdb数据库表清单为：','\n',formlist1)