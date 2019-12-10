from sqlalchemy import create_engine
import pandas as pd
#创建一个MYSQL连接器，用户名为root,密码为1234
#地址为127.0.0.1,数据库名称为testdb,编码为UTF-8
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')

#使用read_sql_table读取订单详情表
detail1 = pd.read_sql_table('meal_order_detail1',con = engine)
#print('使用read_sql_table读取订单详情表的长度为：',len(detail1))#行数
order = pd.read_csv('D:/python/czpython/meal_order_info.csv',encoding = 'gbk') #  = 为赋值， ==为等于
user = pd.read_excel('D:/python/czpython/users.xlsx')
print('订单详情表的维度为；',detail1.ndim)
print('订单信息表的维度为；',order.ndim)
print('客户信息表的维度为；',user.ndim)

print('订单详情表的形状为；',detail1.shape)
print('订单信息表的形状为；',order.shape)
print('客户信息表的形状为；',user.shape)

print('订单详情表的元素个数为；',detail1.size)
print('订单信息表的元素个数为；',order.size)
print('客户信息表的元素个数为；',user.size)

print('订单详情表的counts和amounts两列的描述性统计为: \n',detail1.loc[:,['counts','amounts']].describe())
detail1['order_id'] = detail1['order_id'].astype('category')
detail1['dishes_name'] = detail1['dishes_name'].astype('category')
print('订单编号order_id与dishes_name(菜品名称)的描述性统计结果为: \n',detail1[['order_id','dishes_name']].describe())

#定义一个函数去除全为空值的列和标准差为0的列
def dropNullStd(data):
    beforelen = data.shape[1] #shape[1]列的宽度，shape[0]行的高度
    colisNull = data.describe().loc['count'] == 0 #loc['count'] 取count这一行
    for i in range(len(colisNull)):
        if colisNull[i]:
            data.drop(colisNull.index[i],axis = 1,inplace = True)
    stdisZero = data.describe().loc['std'] == 0
    for i in range(len(stdisZero)):
        if stdisZero[i]:  # ???
            data.drop(stdisZero.index[i],axis = 1,inplace = True)
    afterlen = data.shape[1]
    print('去除列的数目为: ',beforelen - afterlen)
    print('去除后数据的形状为: ',data.shape)
#使用dropNullStd对订单详情表进行操作
dropNullStd(detail1)
#使用dropNullStd对订单信息表进行操作
dropNullStd(order)
#使用dropNullStd对客户信息表进行操作
dropNullStd(user)
