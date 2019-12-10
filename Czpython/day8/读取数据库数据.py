#导入sqlalchemy库的creat_engine函数
from sqlalchemy import create_engine
import pandas as pd
#创建一个mysql连接器，用户名为root,密码为1234
#地址为127.0.0.1，数据库名称为testdb
import warnings
warnings.filterwarnings("ignore")

engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')

#使用read_sql_table读取订单表详情
order1 = pd.read_sql_table('meal_order_detail1',con = engine)
print(len(order1))
order2 = pd.read_sql_table('meal_order_detail2',con = engine)
print(len(order2))
order3 = pd.read_sql_table('meal_order_detail3',con = engine)
print(len(order3))