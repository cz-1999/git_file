import pymysql
import numpy as np
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='barn_sum', charset='utf8')
cursor = conn.cursor()


#计算一个分仓库中任意两个点温度的欧式距离，（欧式距离是确定相关性系数的一种方法），把一个分仓库内的点温度按三维的形式存，
# 然后索引出任意两个点的温度，用欧式距离的公式计算出欧式距离
def cz(table_name,x,y,z,r,c,l):
    sql = '''select `row`,`column`,`layer` from `{}`'''
    cursor.execute(sql.format(table_name))
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
    print(np.array(row).max(),np.array(column).max(),np.array(layer).max())

    sum_row = []

    for i in range(np.array(row).min(),np.array(row).max()+1):
        sum_column = []
        for j in range(np.array(column).min(),np.array(column).max()+1):
            sum_layer = []
            sql = '''select `temperature` from `{}` where `row` = {} and `column`= {} and `layer`= {} '''
            for k in range(np.array(layer).min(),np.array(layer).max()+1):
                data = []
                cursor.execute(sql.format(table_name,i,j,k))
                for k in cursor.fetchall():
                    data.append(k[0])
                sum_layer.append(data)
            sum_column.append(sum_layer)
        sum_row.append(sum_column)
    num1 = np.array(sum_row[x - 1][y - 1][z - 1])
    num2 = np.array(sum_row[r - 1][c - 1][l - 1])
    result = num1 - num2
    print(np.sqrt(np.sum(np.square(result))))

if __name__ == '__main__':
    print('计算任意两点的欧式距离')
    table_name = input('请输入要提取数据的仓库名', )
    x1 = int(input('请输入第一个点的行数',))
    y1 = int(input('请输入第一个点的列数',))
    z1 = int(input('请输入第一个点的层数',))
    r1 = int(input('请输入第二个点的行数',))
    c1 = int(input('请输入第二个点的列数',))
    l1 = int(input('请输入第二个点的层数',))
    cz(table_name,x1,y1,z1,r1,c1,l1) #参数名与变量名不要相同
    conn.commit()
    cursor.close()
    conn.close()
