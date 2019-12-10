#引入模块
from day35 import creat_table
from day35 import insert_table
from day35 import tablename
from day35 import filed  #主目录里面的模块可以直接 import moudle 引用,子目录里面的模块要 from filename import moudle才能引用
from day35 import draw

if __name__ == '__main__':
    print('绘制粮仓内某一点温度随时间的变化曲线')
    table_name = input('请输入用来绘图的表名',)
    row = str(input('请输入要绘制点的行数',))
    layer = str(input('请输入要绘制点的层数',))
    column = str(input('请输入要绘制点的列数',))
    #在barn_sum中创建总表
    creat_table.creat(tablename.fetch_tablene()[0]) #执行完一个函数后，该函数在内存中被清空，执行完之后要提交
    #将barn中的分表插入到barn_sum中的两张总表中
    insert_table.insert(tablename.fetch_tablene()[0],tablename.fetch_tablene()[1])
    #绘制barn_sum中的表中某一点的温度随时间变化的散点图
    draw.draw1(filed.fetch_filed(table_name,row,layer,column)[0],
               filed.fetch_filed(table_name,row,layer,column)[1],
               filed.fetch_filed(table_name,row,layer,column)[2],
               table_name,row,layer,column)

