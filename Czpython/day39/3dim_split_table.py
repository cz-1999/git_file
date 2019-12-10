import pymysql
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei' #设置中文显示
plt.rcParams['axes.unicode_minus'] = False #保证字符正常显示
from pandas.core.frame import DataFrame
from scipy import stats #求众数
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='barn', charset='utf8')
cursor = conn.cursor()

#提取某一仓库内任意 一条线 或者 一个面的温度的均值
#把一维数据存成三维数据,再索引出相应的线或者面的温度求均值，先找出仓库内由多少行，列，层，一个分仓库内温度是以一维的方式存成一列，通过一层索引就能得到温度；要把温度按三维的形式存放，就是通过行列层
#三维索引得到温度，先把温度按层把点存成一条线，再把一条线按列存成一个面，最后把面按行存成一个体，这样就能存储整个仓库内的所有点的温度

#计算出一个仓库内的行，层，列
def num(table_name):
    sql = '''select `row`,`column`,`layer` from `{}`''' #sql语句提取一个仓库内的所有行
    cursor.execute(sql.format(table_name)) #执行sql语句
    #把行层列里面的数据提取出来，存到三个空列表里
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
    #求出3个列表里面的最大值，即一个仓库内行，层，列的个数
    print('仓库总行数:', np.array(row).max(), '仓库总列数:', np.array(column).max(), '仓库总层数:', np.array(layer).max())
    return np.array(row).min(),np.array(row).max(),np.array(column).min(),np.array(column).max(),np.array(layer).min(),np.array(layer).max()


#计算仓库内任意 一条线 或者 一个面的温度的均值
def cz(table_name,r,c,l):
    sql = '''select `row`,`column`,`layer` from `{}`''' #sql语句提取一个仓库内的所有行
    cursor.execute(sql.format(table_name))#执行sql语句
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

    #3层循环，把温度存成3维数据，先按层存，再按列存，最后按行存，先把温度沿着z轴存，再沿着y轴存，再沿着x轴存
    sum_row = []
    for i in range(np.array(row).min(),np.array(row).max()+1):#行循环，把所有面用append()函数存到一个列表，存成一个体
        sum_column = []
        for j in range(np.array(column).min(),np.array(column).max()+1):#列循环，把所有线用append()函数存到一个列表，存成一个面
            sum_layer = []
            sql = '''select `temperature` from `{}` where `row` = {} and `column`= {} and `layer`= {} '''
            for k in range(np.array(layer).min(),np.array(layer).max()+1): #根据层数进行循环
                cursor.execute(sql.format(table_name,i,j,k)) #执行sql语句
                for k in cursor.fetchall(): #获取层上一点的温度，存到列表里
                    sum_layer.append(k[0])
            sum_column.append(sum_layer)
        sum_row.append(sum_column)

    #判断语句，根据输入内容，索引出相应的线或者面的温度，然后用np.array()转换成数组，然后用np.ravel()函数展平为一位数组，然后用np.mean()函数求温度均值
    if r==':'and c!=':'and l!=':':
        print(DataFrame({'a' : np.array(sum_row[:][int(c)-1][int(l)-1]).ravel()}).describe())
        label = ['temperature']  # 定义标签
        gdp = (np.array(sum_row[:][int(c)-1][int(l)-1]).ravel())
        plt.figure(figsize=(8, 7))
        plt.boxplot(gdp, notch=True, labels=label, meanline=True)  # 绘制箱线图
        plt.title('粮仓温度分布箱线图')
        plt.savefig('D:\python\czpython\save_barn_temperature.png')
        plt.show()
    elif c==':'and r!=':'and l!=':':
        print(DataFrame(np.array(sum_row[int(r)-1][:][int(l)-1]).ravel().describe()))
    elif l==':'and c!=':'and r!=':':
        print(DataFrame(np.array(sum_row[int(r)-1][int(c)-1][:]).ravel().describe()))
    elif r==':'and c==':'and l!=':':
        print(DataFrame(np.array(sum_row[:][:][int(l)-1]).ravel().describe()))
    elif r==':'and l==':'and c!=':':
        print(DataFrame(np.array(sum_row[:][int(c)-1][:]).ravel().describe()))
    elif c==':'and l==':'and r!=':':
        print(DataFrame(np.array(sum_row[int(r) - 1][:][:]).ravel().describe()))
    elif c==':'and l==':' and r==':':
        print(DataFrame({'a' : np.array(sum_row[:][:][:]).ravel()}).describe())
        label = ['temperature']  # 定义标签
        gdp = (np.array(sum_row[:][:][:]).ravel())
        plt.figure(figsize=(8, 7))
        plt.boxplot(gdp, notch=True, labels=label, meanline=True)  # 绘制箱线图
        plt.title('粮仓温度分布箱线图')
        plt.savefig('D:\python\czpython\save_barn_temperature.png')
        plt.show()
    else:
        print(DataFrame(np.array(sum_row[int(r)-1][int(c)-1][int(l)-1]).ravel().describe()))


if __name__ == '__main__':
    print('提取某一仓库内任意 一条线 或者 一个面 或者 整个仓库的温度的均值,平均数，四分位数等\n')
    table_name = input('请输入要提取数据的仓库名', )
    num(table_name)
    print('若选择所有行或层或列，请输入\' : \' (英文)')
    r = input('请输入行数',)
    c = input('请输入列数',)
    l = input('请输入层数',)
    cz(table_name,r,c,l)
    conn.commit()
    cursor.close()
    conn.close()
