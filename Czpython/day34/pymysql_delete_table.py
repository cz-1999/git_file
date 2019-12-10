import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='1234',db='barn',charset='utf8')
cursor = conn.cursor()
sql = 'show tables'
cursor.execute(sql)
s=[]
for i in cursor.fetchall():
    s.append(i[0])

sql = 'DROP TABLE IF EXISTS `{}`'
for i in s:
    cursor.execute(sql.format(i))
    conn.commit()

conn.commit()
cursor.close()
conn.close()