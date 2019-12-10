#用sqlalchemy连接mysql数据库
from sqlalchemy import create_engine
#创建一个mysql连接器，用户名为root,密码为1234
#地址为127.0.0.1,数据库名称testdb,编码为utf-8
#要安装pymysql库，才能进行连接

engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/testdb?charset=utf8') #必须是这个格式要换行
print(engine)

