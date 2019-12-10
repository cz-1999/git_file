#请求MySQL数据库
import pymysql
## 打开数据库连接
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='1234',db='barn',charset='utf8')
#使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

#sql更新语句
sql = 'update `1` set `column` = 1+1 where `row` = 6'
try:
    #执行sql语句
    cursor.execute(sql)
    #提交到数据库执行
    conn.commit()
except:
    #如果发生错误则回滚
    conn.rollback()
#对数据进行查找
print(cursor.execute('select * from `1`'))
print(cursor.fetchall())
'''
执行几次更新几次
'''
#提交,不然无法保存新建或者修改的数据
conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()
