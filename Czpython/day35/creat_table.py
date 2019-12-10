#请求MySQL数据库
import pymysql
## 打开数据库连接
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='1234',db='barn',charset='utf8')
#使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

#创建新的总表

def creat(s1):
    #sql语句创建表
    creat = '''
    CREATE TABLE barn_sum.`{}` (
      `barn_id` varchar(254) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
      `barn_name` varchar(254) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
      `time` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
      `row` int(225) NOT NULL,
      `layer` int(225) NOT NULL,
      `column` int(225) DEFAULT NULL,
      `temperature` double(225,2) DEFAULT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci
    '''
    #sql语句，如果表已经存在，则删除
    sql = 'DROP TABLE IF EXISTS barn_sum.`{}`'
    # s1 中是要创建的总表名
    #format语句替换掉 creat 中的 {},用s1中的表名代替，循环创建表
    for i in s1:
        #cursor.execute()函数执行sql语句
        cursor.execute(sql.format(i))
        cursor.execute(creat.format(i))
        #提交对表的修改
        conn.commit()
# 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
if __name__ == '__main__':
    creat()
    conn.commit()
    cursor.close()
    conn.close()