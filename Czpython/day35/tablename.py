#导入正则表达式模块
import re
#请求MySQL数据库
import pymysql
## 打开数据库连接
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='1234',db='barn',charset='utf8')
#使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

def fetch_tablene():
    #sql语句获取数据库内的所有表名
    sql = 'show tables'
    #执行sql语句
    cursor.execute(sql)
    #print(cursor.fetchall()) # 这个执行之后，后面就获取不到数据了，需要再执行一遍sql语句

    #将表名存到列表 s 里面
    s = []
    for i in cursor.fetchall():
        s.append(i[0])

    #用正则表达式匹配要创建的总表名,将表名存到列表 s1 里面
    s1 = []
    for i in s:
        #  '.*[棚库]',这种适用性不高， '(.*?)_\d{4}'适用性很好
        re.search('(.*?)_\d{4}',i).group(1)  #正则表达式匹配要创建的总表名
        s1.append(re.match('(.*?)_\d{4}',i).group(1))
    #返回去重后的总表名 和 barn库中所有的表名  是以元组的形式返回的
    return set(s1),s

# 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
if __name__ == '__main__':
    fetch_tablene()