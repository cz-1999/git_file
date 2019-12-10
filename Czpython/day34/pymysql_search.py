import re
import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='1234',db='barn',charset='utf8')
cursor = conn.cursor()

sql = 'show tables'
cursor.execute(sql)
s = []
for i in cursor.fetchall():
    s.append(i[0])
s1 = []
for i in s:
    s1.append(re.search('.*[棚库]',i).group())
sql = '''select `temperature`,`time` from `上河湾分库_1号罩棚` where `row` = 6 and `layer`=1 and `column`=1'''
print(cursor.execute(sql))

time = []
temperature = []

for i in cursor.fetchall():
    time.append(i[1])

cursor.execute(sql)

for i in cursor.fetchall():
    temperature.append(i[0])

print(time,'\n',temperature)

cursor.close()
conn.close()