#导入正则表达式模块
import re
#请求MySQL数据库
import pymysql
## 打开数据库连接
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='1234',db='barn',charset='utf8')
#使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

#获取数据库内的所有表名
sql = 'show tables'
print(cursor.execute(sql))
#print(cursor.fetchall()) # 这个执行之后，后面就获取不到数据了，需要再执行一遍sql语句
s = []
for i in cursor.fetchall():
    print(i[0])
    s.append(i[0])
print(s)
s1 = []
for i in s:
    print(re.search('.*[棚库]',i).group())
    s1.append(re.search('.*[棚库]',i).group())
print(set(s1))

#将其他库中的表的数据批量插入添加到另一个库的表中
'''
jkdb.factory中的jkdb为数据库，factory为表名 
两张表的字段和字段类型需要一致。
INSERT INTO jkdb.factory SELECT * FROM jb33.factoryc

建立与old_database的连接
在new_database里面创建表，判断表是否存在，只需要在表名前面加上新数据库的名字及 .
举个栗子  
creat table new_database.`table_name` (

)
drop table if exists new_database.`table_name`  一般都将table_name（表名）,filed_name（字段名） 放到 ``内

'''


#创建新的总表
creat = '''
 CREATE TABLE barn_sum.`{}` (
`barn_id` varchar(254) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
`barn_name` varchar(254) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
`time` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
`row` int(225) NOT NULL,
`layer` int(225) NOT NULL,
`column` int(225) DEFAULT NULL,
`temperature` double(225,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
'''
sql = 'DROP TABLE IF EXISTS barn_sum.`{}`'
for i in set(s1):
    cursor.execute(sql.format(i))
    cursor.execute(creat.format(i))
    conn.commit()

#将分表插入到总表
sql = '''INSERT INTO barn_sum.`{}` SELECT * FROM `{}`'''
for i in set(s1):
    for j in s:
        if re.search('.*[棚库]',j).group()== i:
            cursor.execute(sql.format(i,j))
            conn.commit()

conn.commit()
cursor.close()
conn.close()



'''
在MySQL中，我知道我可以用以下方法列出数据库中的表：
SHOW TABLES

获取所有表的名称使用：
SELECT table_name FROM information_schema.tables;
要从特定数据库中获取表的名称，请使用：
SELECT table_name FROM information_schema.tables where table_schema='<your_database_name>';
现在，要回答原始问题，请使用以下查询：
INSERT INTO <table_name> 
    SELECT table_name FROM information_schema.tables
        WHERE table_schema = '<your_database_name>';
'''