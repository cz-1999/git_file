import pymysql
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='barn_sum', charset='utf8')
cursor = conn.cursor()

#接收参数，time,temperature用来绘图的x轴,y轴数据, 用cursor.execute()函数来执行sql语句，确定x轴要设置多少刻度,
#table_name,row,layer,column确定标题名称
def draw1(sql,time,temperature,table_name,row,layer,column):
    #绘制画布大小
    plt.figure(figsize=(8, 6))
    #绘制散点图
    plt.scatter(range(0, cursor.execute(sql),1),temperature, marker='o')
    #x轴标签
    plt.xlabel('时间')
    #y轴标签
    plt.ylabel('温度')
    #y轴刻度范围
    plt.ylim((-30,30))
    #x轴的刻度
    plt.xticks(range(0, cursor.execute(sql),1),time, rotation=45)
    #图形标题
    plt.title('{}_{}行_{}层_{}列点温度变化散点图'.format(table_name,row,layer,column))
    #保存图形
    plt.savefig('D:/python/czpython/save_temperature.png')
    #展示
    plt.show()
# 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
if __name__ == '__main__':
    draw1()
    conn.commit()
    cursor.close()
    conn.close()
