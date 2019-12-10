
import re
import pymysql


class Base:
    """
    数据库操作类
    """

    def __init__(self, MYSQL_HOST, MYSQL_USER, PASSWORD, DATABASE_NAME, MYSQL_PORT):
        self.host = MYSQL_HOST
        self.user = MYSQL_USER
        self.password = PASSWORD
        self.db = DATABASE_NAME
        self.port = MYSQL_PORT

        self.GetConnect()



    def GetConnect(self):
        """
        连接数据库
        :return:
        """
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, db= self.db)
            self.cursor = self.conn.cursor()
        except Exception as err:
            print("数据库连接失败!," , err)



    def Close(self):
        """
        关闭数据库连接
        :return:
        """

        if self.conn:
            try:
                if(type(self.cursor) == 'object'):
                    self.cursor.close()
                if type(self.conn) == 'object':
                    self.conn.close()
            except Exception as err:
                raise("数据库关闭失败，", err)



    def Insertmany(self, table_name,data):
        """
        批量插入数据
        :param data:
        :return:
        """
        print(data)
        sql = "insert into `{}`(`barn_id`, `barn_name`, `time`, `row`, `layer`, `column`, `temperature`) VALUES (%s, %s, %s, %s, %s, %s, %s);".format(pymysql.escape_string(table_name))
        try:
            self.cursor.executemany(sql, data)
            self.conn.commit()
            print("入库成功！")
        except Exception as err:
            #有异常，回滚事务
            self.conn.rollback()


    def combine(self, tables, new_table_names, base):
        """
        mysql 多表合并
        :param tables:  需要合并的tables名称列表
        :param base: 新表存储位置
        :param table_name: 合并表命
        :return:
        """
        newdb_name = base.db

        for new_table_name  in new_table_names:
            #创建总表
            self.creat_table(newdb_name, new_table_name)
            for table in tables:
                if new_table_name in table:
                    #插入表
                    self.insert_to_new_table(newdb_name, new_table_name, table)


    def get_tables_name(self):
        """
        获取所有仓库名
        :return:
        """
        sql = "show tables"

        self.cursor.execute(sql)
        tables = self.cursor.fetchall()

        tables_name = []
        for table in tables:
            tables_name.append(table[0])

        return tables_name


    def new_barn(self, barn_times):
        """
        正则表达式提取仓裤名
        :param barn_times:[[上河湾分库_2号库_2019_04_03_09_18_34]...]
        :return:
        """

        p = '(.*?)_\d{4}'

        barns = []
        for table_name in barn_times:
            #print(table_name)
            barns.append( re.match(p, table_name).group(1))

        print("仓库：",set(barns))
        return set(barns)



    def creat_table(self, db, table_name):
        """
        创建一个数据表
        :param db:数据库名
        :param table_name:
        :return:
        """

        try:
            creat = '''
                    CREATE TABLE {}.`{}` (
                      `barn_id` varchar(254) CHARACTER SET UTF8MB3 COLLATE utf8_unicode_ci NOT NULL,
                      `barn_name` varchar(254) CHARACTER SET UTF8MB3 COLLATE utf8_unicode_ci NOT NULL,
                      `time` varchar(255) CHARACTER SET UTF8MB3 COLLATE utf8_unicode_ci NOT NULL,
                      `row` int(225) NOT NULL,
                      `layer` int(225) NOT NULL,
                      `column` int(225) DEFAULT NULL,
                      `temperature` double(225,2) DEFAULT NULL
                    )
                    '''.format(db, table_name)

            sql = 'DROP TABLE IF EXISTS {}.`{}` '.format(db, table_name)
            self.cursor.execute(sql)  # 之前创建则删除
            self.cursor.execute(creat)
            # 提交对表的修改
            self.conn.commit()
        except Exception as err:
            self.conn.roollback()
            print(err.args)


    def insert_to_new_table(self, db, new_table, table):
        """
        插入数据到新表格中
        :param db: 插入的数据库
        :param new_table: 新表名
        :param table: 表名
        :return:
        """
        try:
            sql = 'INSERT INTO {}.`{}` SELECT * FROM `{}` '.format(db, new_table, table)
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as err:
            print("插入失败", err.args)
            self.conn.rollback()


    def point_temperate(self, barn_name, row, layer, column):
        """
        获取某点的温度（时间序列）
        :return:
        """
        try:
            sql = '''select `barn_name`,`temperature`,`time` from `{}` where `row` = {} and `layer`= {} and `column`= {}'''

            self.cursor.execute(sql.format(barn_name, row, layer, column))

            # cursor.fetchall()返回的数据是二维元组((temperature,time),(temperature,time))
            # 用循环索引提取的时间和温度数据存到相应的列表里
            time = []
            temperature = []
            result = self.cursor.fetchall()
            for i in result:
                time.append(i[2])

            for i in result:
                temperature.append(i[1])


            return barn_name, time, temperature

        except Exception as err:
            print("搜索失败", err.args)






if __name__ == '__main__':
    a = Base('127.0.0.2', 'root', '2333333', 'barn', 3306)
    names = a.get_tables_name()
    a.new_barn(names)