import pymysql
import numpy as np
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='barn_sum', charset='utf8')
cursor = conn.cursor()

#把总仓库中一个点的温度的时间序列存成三维数据，总仓库内一个点温度的时间序列用列表存起来可以看作是一个点，然后按行列层的形式是存起来
#先找出仓库内由多少行，列，层，然后用4层循环将数据存起来
def cz(table_name):
    sql = '''select `row`,`column`,`layer` from `{}`'''  # sql语句提取一个仓库内的所有行
    cursor.execute(sql.format(table_name))  # 执行sql语句
    # 把行层列里面的数据提取出来，存到三个空列表里
    row = []
    column = []
    layer = []
    for i in cursor.fetchall():
        row.append(i[0])
    cursor.execute(sql.format(table_name))
    for i in cursor.fetchall():
        column.append(i[1])
    cursor.execute(sql.format(table_name))
    for i in cursor.fetchall():
        layer.append(i[2])
    # 求出3个列表里面的最大值，即一个仓库内行，层，列的个数
    print('仓库总行数:', np.array(row).max(), '仓库总列数:', np.array(column).max(), '仓库总层数:', np.array(layer).max())

    sum_row = []
    for i in range(np.array(row).min(),np.array(row).max()+1):#根据行数确定循环次数
        print(i)
        sum_column = []
        for j in range(np.array(column).min(),np.array(column).max()+1):#根据列数确定循环次数
            print(j)
            sum_layer = []
            sql = '''select `temperature` from `{}` where `row` = {} and `column`= {} and `layer`= {} ''' #sql语句提取总仓库里点的时间序列
            for k in range(np.array(layer).min(),np.array(layer).max()+1): #根据层数确定循环次数
                print(k)
                data = []
                cursor.execute(sql.format(table_name,i,j,k))#执行sql语句
                for k in cursor.fetchall(): #把一个点在一段时间内的的时间序列，存进data列表里
                    print(k[0])
                    data.append(k[0])
                sum_layer.append(data)  #把data列表存到sum_layer列表里
            sum_column.append(sum_layer)
        sum_row.append(sum_column)
        print(sum_row)

if __name__ == '__main__':
    table_name = input('请输入要提取数据的仓库名', )
    cz(table_name)
    conn.commit()
    cursor.close()
    conn.close()
