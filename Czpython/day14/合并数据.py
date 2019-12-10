#索引完全相同时的横向堆叠为
#行索引
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import mysql.connector
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')
detail1 = pd.read_sql_table('meal_order_detail1',con = engine)

df1 = detail1.iloc[:,:10]#取出detail的前10列数据
df2 = detail1.iloc[:,10:]#取出detail的后9列数据
print('合并df1的大小为%s,df2的大小为%s'%(df1.shape,df2.shape)) # 没有,
print('外连接合并后数据框大小为 :',pd.concat([df1,df2],axis=1,join='outer').shape)
print('内连接合并后数据框大小为 :',pd.concat([df1,df2],axis=1,join='inner').shape)

#纵向堆叠
#对比横向堆叠，纵向堆叠是将两个数据表在y轴上拼接，
#concat函数和append方法两者都可以实现纵向堆叠
#使用concat函数时,在默认情况下,即axis = 0时，concat做列队齐，
# 将不同行索引的两张或多张表纵向合并


#表名完全相同时concat纵向堆叠
df3 = detail1.iloc[:1500,:]
df4 = detail1.iloc[1500:,:]
print('合并df3的大小为%s,df4的大小为%s'%(df3.shape,df4.shape))
print('外连接纵向合并后数据框大小为',pd.concat([df3,df4],axis=0,join='outer',).shape)
print('内连接纵向合并后数据框大小为',pd.concat([df3,df4],axis=0,join='inner',).shape)

#append方法也可以用于纵向合并两张表
#但是使用append方法有一个前提条件,那就是两张表列名需要完全一致

#使用append方法进行纵向表的堆叠
print('堆叠前df3的大小为%s,df4的大小为%s'%(df3.shape,df4.shape))
print('append纵向堆叠后的数据框大小为；',df3.append(df4).shape)

order =pd.read_csv('D:/python/czpython/meal_order_info.csv',encoding='gb18030')#读取订单信息表

#将info_id转换为字符串格式为合并做准备
order['info_id'] = order['info_id'].astype('str')#dataframe转换数据类型
print(order['info_id'].dtypes) #转换后数据类型没变?
#订单详情表和订单信息表都有订单编号
#订单详情表中为order_id,在订单信息表中为info_id
order_detail = pd.merge(detail1,order,left_on='order_id',right_on='info_id')
print('detail订单详情表的原始形状为 ：\n',detail1.shape)
print('order订单信息表的原始形状为: \n',order.shape)
print('订单详情表与订单信息表主键合并后的形状为:\n',order_detail.shape)

#除了使用merge函数以外,join方法也可以实现部分主组键合并功能
#但是使用join方法时，两个主键的名字必须相同，其具体用法如下

order.rename({'info_id':'order_id'},inplace=True) #把info_id替换为order_id
#detail1['order_id'] = detail1['order_id'].astype('str')

#order_detail1 = detail1.join(order,on='order_id',rsuffix='1')
#print('订单详情表和订单信息表join合并后的形状为 :',order_detail1.shape)    #??????????????????????????

#重叠合并数据
#建立两个字典,除了ID外别的特征互补
dict1 = {'ID':[1,2,3,4,5,6,7,8,9],'System':['win10','win10',np.nan,'win10',np.nan,np.nan,'win7','win7','win7'],
         'cpu':['i7','i5',np.nan,'i7',np.nan,np.nan,'i5','i5','i3']}
dict2 = {'ID':[1,2,3,4,5,6,7,8,9],'System':[np.nan,np.nan,'win7',np.nan,'win8','win7',np.nan,np.nan,np.nan],
         'cpu':[np.nan,np.nan,'i3',np.nan,'i7','i5',np.nan,np.nan,np.nan]}
#转换两个字典为DataFrame
df5 =pd.DataFrame(dict1)
df6 =pd.DataFrame(dict2)
print('经过重叠后的数据为: \n',df5.combine_first(df6))

#任务实现
#堆叠不同时间的订单表详情
#读取数据
detail2 = pd.read_sql_table('meal_order_detail2',con =engine)
detail3 = pd.read_sql_table('meal_order_detail3',con =engine)
#纵向堆叠3张表
detail = detail1.append(detail2)
detail = detail.append(detail3)
print('3张订单详情表合并后的形状为: ',detail.shape)

#订单详情表，订单信息表，客户信息表主键合并
user = pd.read_excel('D:/python/czpython/userinfo.xlsx')#读取客户信息表
#数据类型转换，存储部分数据

order['info_id'] = order['info_id'].astype('str')
order['emp_id'] = order['emp_id'].astype('str')
user['USER_ID'] = user['USER_ID'].astype('str')
data = pd.merge(detail,order,left_on=['order_id','emp_id'],right_on=['info_id','emp_id'])#使用两个主键进行合并
data = pd.merge(data,user,left_on='emp_id',right_on='USER_ID',how = 'inner')
print('3张表数据主键合并后的大小为：',data.shape)#数据对不上??????











































