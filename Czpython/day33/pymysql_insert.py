#请求MySQL数据库
import pymysql
#打开数据库连接
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='1234',db='barn',charset='utf8')
#使用 cursor() 方法创建一个游标对象 cursor 中文: 计算机上的 光标，游标，指针
cursor = conn.cursor()

#数据库插入操作
# SQL 插入语句
sql = '''INSERT INTO `1` VALUES ('40288146688299ea016882bff2f0001d', '上河湾分库_1号罩棚', '2019_02_18_09_35_41', 6, 1, 1, -4.38)'''

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()  #可以直接在最后一步提交，这一步可以省略
except:
    # 如果发生错误则回滚
    cursor.rollback()
#对数据进行查找
#
print(cursor.execute('select * from `1`'))
print(cursor.fetchall())
'''
执行了几次就插入几个
'''
# pymysql.connect 类默认开启了事务，因此对表进行修改、更新、删除、插入操作时需要提交事务才可以生效
# 提交，不然无法保存新建或者修改的数据

'''执行事务: 对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。      
commit()  方法游标的所有更新操作         
rollback(）方法回滚当前游标的所有操作。
每一个方法都开始了一个新的事务。

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()  #可以直接在最后一步提交，这一步可以省略
except:
    # 如果发生错误则回滚,撤销游标的所有操作
    cursor.rollback()
'''

conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()

