import pandas as pd
import os
#使用read_excel读取菜品订单信息表
user = pd.read_excel('D:/python/czpython/users.xlsx')#读取users.xlsx文件 #一般用 / 来指示路径  \ 容易跟转义字符弄混
#像 \t 就可能转义为 tab 键
print('客户信息表长度为：',len(user))

#使用to_excel函数将数据存储为Excel文件
print('客户信息表写入Excel文件前，目录内文件列表为: \n',os.listdir('D:\python\czpython'))
user.to_excel('D:/python/czpython/userInfo.xlsx')
print('客户信息表写入Excel文件后，目录内文件列表为: \n',os.listdir('D:\python\czpython'))