#合并数据, 对象dataframe
# 横向或纵向合并数据
# 主键合并数据
# 重叠合并数据
# 堆叠合并数据
# 堆叠就是简单的把两张表拼接在一起，也被称作轴向连接，绑定，或连接，依照连接轴的方向，数据堆叠可分为 横向堆叠 和 纵向堆叠
#横向堆叠，两张表在x轴向拼接在一起，使用concat函数，常用3个参数：
# objs:接收series,dataframe,panel的组合，表示参与连接的pandas对象的 '列表' 的组合，无默认
# axis:接收 0或1 表示连接轴向，默认为0，列，
# join:接收inner或outer,表示其它轴上的索引是按交集还是按并集进行合并的,默认为outer
#当axis = 1时，concat做行对齐，然后将不同列名称的两张表或多张表合并，当两张表索引不完全一样时，可以使用join参数选择内连接接还是外连接
#内连接按行索引的交集进行合并，外连接按行索引的并集进行合并，当两张表完全一样时，不论join参数的取值是inner或者outer结果都是将两张表完全按x轴拼接起来
#pd.concat([dataframe,dataframe],axis=1,join='outer')

from sqlalchemy import create_engine
import pandas as pd
import numpy as np
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/testdb?charset=utf8')
detail = pd.read_sql('meal_order_detail1',con=engine) #  con= 可以省略不写
df1 = detail.iloc[:,0:10] #用iloc,可以接收列位置,loc只能结束列名
df2 = detail.iloc[:,10:]
print(df1.shape)
print(df2.shape)
print(pd.concat([df1,df2],axis=1,join='outer').shape)#外连接
print(pd.concat([df1,df2],axis=1,join='inner').shape)#内连接
#当axis=0时，concat做行对齐，然后将不同行索引的两张或多张表纵向合并.在两张表列名并不完全相同的情况下,可以使用join参数
#选择内连接(join=inner)或者外连接(join=outer),内连接只返回列名的交集,外连接返回列名的并集
df3 = detail.iloc[0:1500,:]
df4 = detail.iloc[1500:,:]
print(df3.shape)
print(df4.shape)
print(pd.concat([df3,df4]).shape)
#append函数,也可以用于纵向合并两张表,有一个前提条件,两张表的列名需要完全一致
#other 接收dataframe或series,表示要添加的新数据,无默认
#ignore_index 接收boolean如果输入True就会对新生成的dataframe使用新的索引(自动产生)而忽略原来数据的索引,默认为False
#verify_integrity 接收boolean,如果输入True当,ignore_index为False时,会检查添加的数据索引是否冲突,如果冲突则会添加失败,默认为False
#   dataframe.append(dataframe)
print(df3.append(df4).shape)

#主键合并数据,即通过一个或两个键将两个数据集的行连接起来类似于sql中的join,针对两张包含不同字段的表,将其根据某几个字段一一对应拼接起来,结果集的列数
#为原数据的列数减去连接键的数量
#pandas中的merge函数和join函数都可以是实现主键合并,但是方法不同,和数据库一样的join一样,merge函数也有左连接(一种连接方式),右连接,外连接,内连接,
#左连接: 左边取全部,右边取部分,没有值用NaN填充,右连接:右边取全部,左边取部分,没有值用NaN填充
# 与sql语言的join相比merge函数可以在合并过程中对数据集中的数据进行排序等,
#left 接收dataframe或series 表示要添加的新数据1,无默认
#right 接收dataframe或series 表示要添加的新数据2,无默认
#how 接收inner outer,left right 表示数据连接方式默认为inner
#on 接收string 或sequence 表示两个数据合并的主键,(必须一致)默认为none,两个主键(列名)不一致时,可以用left_on,right_on参数进行指定
#left_on接收string或sequence表示left参数接收数据用于合并的主键,默认为none
#right_on接收string或sequence表示right参数接收数据用于合并的主键,默认为none
#left_index接收boolean 表示是否将left参数,接收数据的index作为连接主键默认为False
#right_index接收boolean 表示是否将right参数,接收数据的index作为连接主键默认为False
#sort 接收boolean表示是否根据连接键对合并后的数据进行排序,默认为False
#suffixes 接收tuple(元组) ,表示用于追加到left和right参数接收数据列名相同时的后缀.默认为('x','y')
#pd.merge(dataframe,dataframe,left_on = 主键,right_on =主键)

#使用merge函数合并数据表,
order = pd.read_csv('D:/python/czpython/meal_order_info.csv',sep=',',encoding='gbk')
#将info_id转为字符串格式,为合并做准备
#object 类：应该被翻译为“对象”，或者“东西”类。object 类是所有类的父类。换言之，其它的任何一个类，
# 都直接或间接地继承了 object 类（的属性和方法）。
order['info_id'] = order['info_id'].astype('str')# 将info_id的类型转换为'str'
detail['order_id'] = detail['order_id'].astype('str')#将order_id的类型转换为'str'
# detail['order_id'] 和 order['info_id']显示的类型认为object类,但是其列的数据类型已经转换成了字符串类型
print(detail['order_id'].dtypes)
print(order['info_id'].dtype)
#订单详情表与订单信息表都有订单编号,order_id, info_id
order_detail = pd.merge(detail,order,left_on='order_id',right_on='info_id')
print(order_detail.shape) #刚好40列,  总的列数 - 作为主键的列数

#join函数实现部分主键合并功能,使用join函数时,两个主键的名字必须相同
#other 接收dataframe,series或者包含了多个dataframe的list表示参与连接的其他dataframe,无默认
#on 接收列名或者包含列名的list或tuple.表示用于连接的列名.默认为none
#how 接收特定的string 取值为inner时代表内连接,outer时代表外连接,即全连接,取值为left时代表左连接,
# 取值为right时代表右连接,默认为inner
#lsuffix 接收string,用于追加到左侧重叠列名的尾缀
#rsuffix 接收string,用于追加到右侧重叠列名的尾缀
#sort 接收boolean 根据连接键,对合并后的数据进行排序
#dataframe.join(dataframe,on='order_id',rsuffix='1')

#使用join实现主键合并

#其中一个dataframe的列名需要改一下,保证主键相同,pd.rename函数
#使用pd.rename函数
#a.rename(columns={'A':'a', 'C':'c'}, inplace = True)1
#上面代码的意思是:
#1,对a这个df进行操作,涉及的列为A和C两列
#2:将涉及的列用字典括起来,’A’:’a’的意思是将原大A列的列名称修改为小a列
#3,inplace指的是直接修改,不使用复制的方式,要是没有inplace这个参数,或者这个参数为False,需要改写成
#a = a.rename({'A':'a', 'C':'c'})

#dataframe.rename(columns={'旧名字':'新名字'},inplace=True)

'''
order.rename(columns = {'info_id':'order_id'},inplace=True)
print(order['order_id'].shape)
order['order_id'] = order['order_id'].astype('str')
order_detail1 = detail.join(order,on= 'order_id',rsuffix='1',how='inner')
print(order_detail1.shape)
'''
#重叠合并数据,数据分析和处理过程中偶尔会出现两份数据内容几乎一致的情况，但是某些特征在其中一张表上是完整的，而另一张表上数据是缺失的除了
#将数据一对一比较外，然后进行填充的方法外，就是重叠合并   combine_first函数，
#一个参数 other :接收dataframe 表示参与重叠合并的另一个dataframe
#dataframe.combine_first(other)

dict1 ={'ID':[1,2,3,4,5,6,7,8,9],'System':['win10','win10',np.nan,'win10',np.nan,np.nan,'win7','win7','win8'],
        'cpu':['i7','i5',np.nan,'i7',np.nan,np.nan,'i5','i5','i3']}
dict2 ={'ID':[1,2,3,4,5,6,7,8,9],'System':[np.nan,np.nan,'win7',np.nan,'win8','win7',np.nan,np.nan,np.nan],
        'cpu':[np.nan,np.nan,'i3',np.nan,'i7','i5',np.nan,np.nan,np.nan]}
#将两个字典转换为dataframe  pd.DataFrame()函数    pd.dataframe(dict)
df5 = pd.DataFrame(dict1)
df6 = pd.DataFrame(dict2)
print(df5.combine_first(df6))

#堆叠不时间的订单详情表
#订单详情表meal_order_detail1,meal_order_detail2,meal_order_detail3具有相同的特征单数据时间不同，订单编号也不同，
#在分析过程中要使用全部数据，需要将几张表做堆叠操作
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/testdb?charset=utf8')
detail1 = pd.read_sql('meal_order_detail1',con = engine)
detail2 = pd.read_sql('meal_order_detail2',con=engine)
detail3 = pd.read_sql('meal_order_detail3',con=engine)
#纵向堆叠3张表
#concat函数
detail = pd.concat([detail1,detail2])
detail = pd.concat([detail,detail3])
print(detail.shape)
#append函数
detail = detail1.append(detail2)
detail = detail.append(detail3)
print(detail.shape)

#主键合并订单详情表，订单信息表，客户信息表，
#这3个表之间存在相同意义的字段，因此需通过主键合并
order = pd.read_csv('D:/python/czpython/meal_order_info.csv',encoding='gb18030')#读取订单信息表
user = pd.read_excel('D:/python/czpython/users_info.xlsx')
order['info_id'] = order['info_id'].astype('str')
order['emp_id'] = order['emp_id'].astype('str')
user['USER_ID'] = user['USER_ID'].astype('str')
data = pd.merge(detail,order,left_on=['order_id','emp_id'],right_on=['info_id','emp_id'])
data = pd.merge(data,user,left_on=['emp_id'],right_on=['USER_ID'],how='inner')
print(data.shape)

