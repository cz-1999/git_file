from sqlalchemy import create_engine
import pandas as pd
#创建一个MYSQL连接器，用户名为root,密码为1234
#地址为127.0.0.1,数据库名称为testdb,编码为UTF-8
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')

#使用read_sql_table读取订单详情表
detail1 = pd.read_sql_table('meal_order_detail1',con = engine)
print('使用read_sql_table读取订单详情表的长度为：',len(detail1))#行数

#更改DataFrame中的数据
#更改DataFrame中的数据的原理是将这部分数据提取出来，重新赋值为新的数据
#将order_id为458的变换为45800
detail1.loc[detail1['order_id']=='458','order_id'] ='45800'
print('更改后detail中order_id为458的order_id为: \n',detail1.loc[detail1['order_id']=='458','order_id'])
print('更改后detail中order_id为45800的order_id为: \n',detail1.loc[detail1['order_id']=='45800','order_id'])
#需要注意的是数据的更改是原数据的直接更改,操作无法撤销,如果做出更改则需要对更改条件进行确认或对数据进行备份

#为DataFrame增添数据
#为DataFrame添加一列数据的方法非常简单,只需要新建一个列索引,并对该索引下的数据进行不赋值操作即可
detail1['payment'] = detail1['counts']*detail1['amounts']
print('detail1新增列payment的前5列为: \n',detail1['payment'].head())
#如果新增的一列值是相同的，则最直接为其赋值一个常量即可
detail1['pay_way'] = '现金支付'
print('detail1新增列pay_way的前5列为: \n',detail1['pay_way'].head())

#删除某行或某列的数据
#删除DataFrame某列
print('删除pay_way前的detail1的索引为 \n',detail1.columns)
detail1.drop(labels = 'pay_way',axis = 1,inplace = False)
#labels代表删除的行或列的标签，axis代表操作轴向，默认为0,x轴,inplace代表操作是否对原数据数据生效，默认为Falsse
print('删除pay_way后的detail1的索引为 \n',detail1.drop(labels = 'pay_way',axis = 1,inplace = False).columns)
#要删除行某行数据，只需要将drop方法参数中的'labels'参数换成对应的行索引，将axis参数设置为0即可

#删除DataFrame某几行
print('删除1-10行前detail的长度为: ',len(detail1))
detail1.drop(labels = range(1,12),axis = 0,inplace = False)
print('删除1-10行前detail的长度为: ',len(detail1.drop(labels = range(1,11),axis = 0,inplace = False)))