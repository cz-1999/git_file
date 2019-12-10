from sqlalchemy import create_engine
import pandas as pd
import mysql.connector
#用mysql.connector库代替pymysql库连接mysql库可以解决警告

#创建一个mysql连接器，用户名为root,密码为1234
#地址为127.0.0.1,数据库名称为testdb,编码为utf-8
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')
print(engine)

#使用read_sql_query查看testdb中的数据表数目
#formlist = pd.read_sql_query('show tables',con = engine)
#print('testdb数据库数据表清单为:','\n',formlist)

## 使用read_sql_query查看tesdb中的数据表数目
formlist = pd.read_sql_query('show tables', con = engine)
print('testdb数据库数据表清单为:','\n',formlist)