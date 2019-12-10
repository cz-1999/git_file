import pandas as pd

import warnings
warnings.filterwarnings("ignore")
#可以忽略掉警告信息

#使用read_table读取菜单信息表
order = pd.read_table('D:\python\czpython\meal_order_info.csv',sep = ',',encoding = 'gbk') #会有警告
print('使用read_table读取菜品订单信息表长度为',len(order))
#使用read_csv读取菜单信息表
order1 = pd.read_csv('D:\python\czpython\meal_order_info.csv',encoding = 'gbk')
print('使用read_csv读取菜品订单信息表长度为',len(order1))
print(order1)

#更改参数读取菜单信息表
#使用read_tabel读取菜单信息表，sep = ';'
order2 = pd.read_table('D:\python\czpython\meal_order_info.csv',sep = ';',encoding = 'gbk')
print('分隔符为；时菜品订单信息表为：','\n',order2)
#read_rable和read_csv函数中的sep参数是指定文本的分隔符的，如果分隔符指定错误，再读取数据的时候，每行数据将连成一片

#使用read_csv读取菜单订单信息表，header = None,  header参数是用来指定列名的，如果是None,则会添加一个默认的列名
order3 = pd.read_csv('D:\python\czpython\meal_order_info.csv',sep = ',',header = None,encoding = 'gbk')
print('header为None时菜品订单信息表为：','\n',order3)# '\n' 表示换行


#使用utf-8解析菜品订单信息表 encoding表示文件编码格式，如果编码指定错误则数据将无法读取，解释器会报告解释错误
#order4 = pd.read_csv('D:\python\czpython\meal_order_info.csv',sep = ',',encoding = 'utf-8')
#常用的编码有utf-8,utf-16,gbk,gb2312,gb18030等

#使用to_csv函数将数据写入csv文件中
import os
print('菜品订单信息表写入文本文件前目录内文件列表为：','\n',os.listdir('D:\python\czpython'))
#将order以csv文件存储
order.to_csv('D:\python\czpython\orderInfo.csv',sep = ';',index = False)
print('菜品订单信息表写入文本文件后目录内文件列表为: \n',os.listdir('D:\python\czpython'))#直接写\n也能换行
