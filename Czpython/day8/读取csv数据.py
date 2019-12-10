import pandas as pd

#使用read_table读取订单信息表
orderInfo = pd.read_table('D:/python/czpython/orderInfo.csv',sep = ',',encoding = 'utf-8')
print('订单信息表长度为:',len(orderInfo))

