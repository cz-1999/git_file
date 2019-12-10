#请求MySQL数据库
import pymysql
## 打开数据库连接
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='1234',db='barn',charset='utf8')
#使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

#创建数据库
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute('SET NAMES utf8mb4')
cursor.execute('SET FOREIGN_KEY_CHECKS = 0')
cursor.execute('DROP TABLE IF EXISTS `1`')

#使用预处理语句创建表
sql = '''CREATE TABLE `1`  (
  `barn_id` varchar(254) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `barn_name` varchar(254) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `time` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `row` int(225) NOT NULL,
  `layer` int(225) NOT NULL,
  `column` int(225) NULL DEFAULT NULL,
  `temperature` double(225, 2) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic
'''

#执行语句,创建数据库
cursor.execute(sql)
# 提交，不然无法保存新建或者修改的数据
conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()

#不关闭游标和连接也能运行