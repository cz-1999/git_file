import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='1234',db='barn',charset='utf8')
cursor = conn.cursor()

# sql 删除语句
sql = 'delete from `1` where `row` > 0 '  #row 要放到 `` 内才能执行
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()
except:
    # 如果发生错误则回滚,撤销游标的所有操作
    conn.rollback()
#对数据进行查找
print(cursor.execute('select * from `1`'))
print(cursor.fetchall())

# 提交，不然无法保存新建或者修改的数据
conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()