#导入正则表达式模块
import re
#请求MySQL数据库
import pymysql
## 打开数据库连接
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='1234',db='barn',charset='utf8')
#使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

def insert(s1,s):
    #sql语句把barn数据库中的表插入到barn_sum数据库中的总表里，表名前要加上 database_name.
    sql = '''INSERT INTO barn_sum.`{}` SELECT * FROM `{}`'''
    #循环执行sql语句，把s中的分表插入到s1中的总表里,
    for i in s1:    #s1中存放的是barn_sum中已经创建好的总表
        for j in s:  #s中存放的是barn中所有的分表
            if re.match('(.*?)_\d{4}',j).group(1)== i: #用正则表达式匹配表名，将所有分表插入到相应的总表中去

                #  '.*[棚库]',这种适用性不高， '(.*?)_\d{4}'适用性很好

                #format语句替换掉{},换成创建好的总表名，和要插入的分表名
                cursor.execute(sql.format(i,j))
                #提交，保存对数据库的修改
                conn.commit()
#运行的时候要提交，当作模块被调用时，只是执行函数的内容，主函数里面的提交不能保存,包里面数据的更改,主
if __name__ == '__main__':
    insert()
    conn.commit()
    cursor.close()
    conn.close()

