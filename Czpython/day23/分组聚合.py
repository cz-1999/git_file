#依据某个或者某几个字段对数据集进行分组，并对各组应用一个函数，无论是聚合还是转换都是数据分析的常用操作
#panda提供了一个灵活高效的groupby函数用来拆分,配合agg函数或apply函数用来聚合

#group函数提供分组聚合步骤中的拆分功能，能够根据索引或者字段对数据进行分组，常用参数by: 接收list,string,mapping
#或generator，用于确定进行分组的依据 传入的是函数，则对索引进行计算并分组，如果传入的是一个字典或者series，则字典或者series
#用来作为分组依据,如果传入的是一个numpy数组，则数组元素作为分组依据，如果传入的是字符串或者字符串列表，则使用这些字符串代表的
#字段作为分组依据 axis: 接收int 表示操作轴向,默认对行进行操作,axis=0,  dataframe.group(by= )

#group函数可以根据多个字段或索引来进行分组 .group(by = ['order_id','dishes_name'])

#按订单编号进行分组
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/testdb?charset=utf8')
detail = pd.read_sql('meal_order_detail1',con = engine)
detailGroup = detail[['order_id','counts','amounts']].groupby(by = 'order_id')
print(detailGroup)
#分组后的对象不能直接查看，而是被存在内存中，输出的是内存地址，分组后的数据对象GroupBy类似与dataframe,与series
#是pandas提供的一种对象,groupby描述性统计方法可以使用pandas自带的函数，这些函数可以查看经过分组后每一组的均值，标准差
#中位数    groupby.head()返回每组的前n个值，groupby.mean()返回每组的均值

print(detailGroup.mean().head())   #这里的.head()是返回每组的均值的前5行、
print(detailGroup.median().head())
print(detailGroup.std().head())
print(detailGroup.size().head())

#常用3个函数聚合数据agg,apply,transform,一般常用agg函数即可
#使用agg方法聚合数据，agg,aggregate函数都支持对每个分组应用某函数,包含python内置函数或自定义函数
#这两个函数也能直接对dataframe直接进行函数操作,agg函数常用两个参数 func:接收list,dict,function表示应用于每行每列
#的函数，无默认 axis: 接收0或1，0代表列，1代表行，默认为0
#agg函数中可以使用numpy库中的函数         np.函数      函数后面不加()
#agg中可以传入自定义的函数
#dataframe[['counts','amounts']].agg([np,mean,np.sum]) ,
#dataframe.agg({'counts':np.mean,'amounts':np.sum})
#dataframe.agg({'counts':np.mean,'amounts':[np.sum,np.sum]})

#不使用agg函数，对dataframe的某一列进行操作
print(detail.sum()) #直接对整个dataframe进行求和操作,数值型数据直接相加，非数值型数据连在一起

#agg函数的优势在于可以同时对不同的列采取不同的操作
print(detail[['counts','amounts']].agg([np.sum,np.mean]))
print(detail.agg({'counts':np.sum,'amounts':np.mean}))
print(detail.agg({'counts':np.sum,'amounts':[np.mean,np.sum]}))

#agg中使用自定义函数
def doublesum(data):
    s = data.sum()*2
    return s
print(detail.agg({'counts':doublesum}))
#不使用自定义函数
print(doublesum(detail['counts']))
#numpy库中的函数能够在agg中直接使用,但是自定义函数在使用numpy库中的这些函数时
#如果计算的是单个序列则无法的出想要的结果(只是扩大2倍，没有求和)，如果是多列数据同时计算则不会出现这种问题

#自定义函数中含numpy中的函数
def doublesum1(data):
    s = np.sum(data)*2
    return s
print(detail.agg({'counts':doublesum1}))
#多列数据一起计算可以
print(detail[['counts','amounts']].agg(doublesum1))

#agg函数也适用于分组数据,对每一字段每一组使用相同的函数
print(detailGroup.agg(np.mean))
print(detailGroup.agg(np.std))
#对不同字段使用不同的函数，则与dataframe中agg方法的操作相同
print(detailGroup.agg({'counts':np.mean,'amounts':np.sum}))

#使用apply函数聚合数据，apply函数类似与agg函数能够将函数应用于某一列，不同之处在于apply函数只能作用于整个dataframe
#或者series，不能像agg函数一样对不同字段采用不同的函数获得不同的结果，apply函数常用参数，func : 接收functions,list
# 表示应用于每行每列的函数, axis: 0 列  1行 默认为0
#如果计算的是单个序列，得不到想要的结果（把单个序列放到列表里是可以的），计算的是多列数据没有问题

print(detail[['amounts']].apply(np.mean))
print(detail[['amounts','counts']].apply([np.mean,np.sum]))
#apply对groupby对象操作方法于agg类似，apply函数不能实现对不同的字段应用不同的函数
print(detailGroup.apply(np.mean).head(3))
print(detailGroup.apply(np.std).head(3))

#transform函数只有一个参数func,表示对dataframe操作的函数,i
#dataframe.transform(lambda x(自变量):x*2(因变量))，transform的优势在于不用再自定义一个函数
print(detail[['counts','amounts']].transform(lambda x:x*2).head())
#不能直接对dataframe实现离差标准化,对groupby可以
#print(detailGroup[['counts','amounts']].transform(lambda x:(x.mean()-x.min())/(x.max()-x.min())).head())
#结果中部分结果为NaN，最大值与最小值相等，分母为0,python中分母为0的数显示为NaN

#按时间对菜品订单详情表进行拆分
from sqlalchemy import create_engine
import numpy as np
import pandas as pd
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/testdb?charset=utf8')
detail =pd.read_sql('meal_order_detail1',con = engine)
#需要添加一列日期
detail['place_order_time'] = pd.to_datetime(detail['place_order_time'])
detail['date'] = [i.date() for i in detail['place_order_time']]
detailGroup = detail[['date','counts','amounts']].groupby(by ='date')
print(detailGroup.size().head())
#使用agg计算出单日菜品销售平均单价和售价中位数
daymean = detailGroup['amounts'].agg(np.mean)
print(daymean)
daymedian = detailGroup['amounts'].agg(np.median)
print(daymedian)
#使用apply统计单日菜品销售数目
daysalesum = detailGroup['counts'].apply(np.sum)
print(daysalesum)

#透视表与交叉表，数据透视表是数据分析中常见的工具之一，根据一个或多个键值对数据进行聚合，根据行和列的分组键将数据划分到各个区域
#在pandas中除了可以私用groupby对数据分组聚合实现透视功能外，还可以使用更强大的pivot_table函数对数据分组聚合,
#pivot_table函数的参数
# data: 接收dataframe，表示创建表的数据
# values: 接收string 用于指定要聚合的字段名，默认使用全部数据
# index: 接收string或list ,表示行分组建，默认为none
# columns: 接收string或list，表示列分组键，默认为none
# aggfunc: 接收functions 表示聚合的函数，默认为mean
# margins 接收boolean表示汇总功能的开关，设置为True后,结果集中会出现名为ALL的 '行' 和 '列' 。默认为True,有时候不设置为margins = True不显示
# dropna 接收boolean。表示是否删掉全为NaN的列。默认为False
#pd.pivot_table(dataframe[''],index='')
#当不特殊指定聚合函数aggfunc时，会默认使用np,mean进行聚合计算，np.mean会自动过滤掉非数值类型数目,可以通过aggfunc参数来修改聚合函数

#使用订单号作为透视表索引制作透视表
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/testdb?charset=utf8')
detail = pd.read_sql('meal_order_detail1',con = engine)
detailpivot = pd.pivot_table(detail[['order_id','counts','amounts']],index='order_id')
print(detailpivot.head())

#修改聚合函数
print(pd.pivot_table(detail[['order_id','counts','amounts']],index='order_id',aggfunc=np.sum))

#与groupby分组方法相同,pivot_table函数在创建透视表时分组键index可以有多个
#使用订单号和菜品名称作为行分组建
print(pd.pivot_table(detail[['order_id','counts','amounts','dishes_name']],index=['order_id','dishes_name'],aggfunc=np.sum))
#两个行分组键，对某个菜的价格和数目进行相加，一个列分组键数据相当于已经汇总过了，所以就没有All列

#通过comluns参数指定列分组，应该会有两个列索引，一个是最上层的amounts和counts,一个是菜品名称
print(pd.pivot_table(detail[['order_id','counts','amounts','dishes_name']],index='order_id',columns = 'dishes_name',aggfunc=np.sum))

#通过values参数来指定自己想要显示的列,其他列不显示
print(pd.pivot_table(detail[['order_id','dishes_name','counts','amounts']],index='order_id',values ='counts',aggfunc=np.sum))

#当数据不存在时会自动填充NaN,可以指定fill_value参数,表示当存在缺失值时以指定数值进行填充
print(pd.pivot_table(detail[['order_id','dishes_name','counts','amounts']],index='order_id',columns='dishes_name',aggfunc=np.sum,fill_value=0))
#更改margins参数，查看汇总数据
print(pd.pivot_table(detail[['order_id','dishes_name','counts','amounts']],index='order_id',columns='dishes_name',values='counts',aggfunc=np.sum,fill_value=0,margins=True))

#使用crosstab函数来创建交叉表，交叉表是一种特殊的透视表，主要用于计算分组频率
#crosstab函数参数和pivot_table函数参数基本相同，不同之处在于crosstab函数中的index,columns,values输入的都是从dataframe中提取的某一列
#若不设置values值则默认对全部数据进行操作
# index: 接收string或list ,表示行分组建，无默认
# columns: 接收string或list，表示列分组键，无默认
# values: 接收array,表示聚合数据，默认为none
# rownames: 表示行分组键名。无默认
# colnames: 表示列分组键名。无默认
# aggfunc: 接收function 表示聚合的函数，默认为none
# margins 接收boolean表示汇总功能的开关，设置为True后,结果集中会出现名为ALL的 '行' 和 '列' 。默认为True,有时候不设置为margins = True不显示
# dropna 接收boolean。表示是否删掉全为NaN的列。默认为False
# normalize 接收boolean。表示是否对值进行标准化。默认为False
#pd.crosstab(index=dataframe[''],columns=dataframe[''],values=dataframe[''],aggfunc=)

#使用crosstab函数制作交叉表
detailcross = pd.crosstab(index=detail['order_id'],columns=detail['dishes_name'],values=detail['counts'],aggfunc=np.sum)

#订单详情表单日菜品成交总额与总数透视表
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/testdb?charset=utf8')
detail = pd.read_sql('meal_order_detail1',con = engine)
detail['place_order_time'] = pd.to_datetime(detail['place_order_time'])
detail['date'] = [i.date() for i in detail['place_order_time']]
detailpivot = pd.pivot_table(detail[['date','amounts','counts']],index='date',aggfunc=np.sum) #要把多个字符段以列表的形式存起来
print(detailpivot)
crossdetail = pd.crosstab(index=detail['date'],columns=detail['dishes_name'],values=detail['amounts'],aggfunc=np.sum,margins=True)
print(crossdetail)
