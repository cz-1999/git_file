import re
import pymysql
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='barn_sum', charset='utf8')
cursor = conn.cursor()

def draw():
    sql = '''select `temperature`,`time` from `上河湾分库_2号库` where `row` = 3 and `layer`=1 and `column`=1'''
    print(cursor.execute(sql))
    time = []
    temperature = []
    for i in cursor.fetchall():
        time.append(i[1])
    cursor.execute(sql)
    for i in cursor.fetchall():
        temperature.append(i[0])
    print(time,'\n',temperature)
    time = np.array(time)
    temperature = np.array(temperature)

    #绘制散点图
    plt.figure(figsize=(8,6))
    plt.scatter(range(0,cursor.execute(sql),1),temperature,marker='o')
    plt.xlabel('时间')
    plt.ylabel('温度')
    plt.ylim((-30,30))
    plt.xticks(range(0,cursor.execute(sql),1),time,rotation=45)
    plt.title('上河湾分库_2号库_3行_1层_1列点温度变化散点图')
    plt.savefig('D:/python/czpython/save_temperature.png')
    plt.show()

if __name__ == '__main__':
    draw()


conn.commit()
cursor.close()
conn.close()


