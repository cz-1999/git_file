import pandas as pd
#读取users.xlsx文件
userInfo = pd.read_excel('D:/python/czpython/users.xlsx',sheetname = 'users1') #文件名，表名，要写对
print('客户信息表的长度为：',len(userInfo))