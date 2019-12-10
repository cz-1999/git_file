import pymysql
import numpy as np
import matplotlib.pyplot as plt
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='barn_sum', charset='utf8')
cursor = conn.cursor()

#设置参数，决定绘制仓库某一点的温度变化曲线
def fetch_filed(table_name,row,layer,column):

    #sql语句，从表中提取符合条件的列，
    sql = '''select `temperature`,`time` from `{}` where `row` = {} and `layer`= {} and `column`= {}'''

    #执行sql语句,从表中提取符合条件的数据
    cursor.execute(sql.format(table_name,row,layer,column))

    #cursor.fetchall()返回的数据是二维元组((temperature,time),(temperature,time))
    #用循环索引提取的时间和温度数据存到相应的列表里
    time = []
    temperature = []
    for i in cursor.fetchall():
        time.append(i[1])
    cursor.execute(sql.format(table_name,row,layer,column))
    for i in cursor.fetchall():
        temperature.append(i[0])

    #把列表强制转换成数组，用来绘图
    time = np.array(time)
    temperature = np.array(temperature)

    #用format语句把sql中的{},用参数替换掉
    sql = sql.format(table_name,row,layer,column)

    #返回sql语句，time数组，temperature数组
    return sql,time,temperature

# 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
if __name__ == '__main__':
    fetch_filed()
    conn.commit()
    cursor.close()
    conn.close()