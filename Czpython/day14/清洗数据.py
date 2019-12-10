#记录重复

#利用list去重
import pandas as pd
#方法一
#定义去重函数

detail = pd.read_csv('D:/python/czpython/detail.csv',index_col=0,encoding='gbk')
def delRep(list1):
    list2=[]
    for i in list1:
        if i not in list2:
           list2.append(i)
    return list2
#去重
dishes = list(detail['dishes_name']) #将dishes_name从数据框中提取出来
print('去重前的菜品总数为: ',len(dishes))
dish = delRep(dishes) #使用自定义函数去重
print('方法一去重后的菜品总数为: ',len(dish))
#方法二
#可以利用集合(set)元素唯一的特性去重
print('去重前的菜品总数为: ',len(dishes))
dish_set = set(dishes) # set对list进行操作，具有去重特性
print('方法二去重后的菜品总数为: ',len(dish_set))

#方法一代码冗长,会拖慢数据分析进度
#方法二会导致数据的排列发生改变
#这两种方法不能修改原数据
print(dish)
print(dish_set)
print(detail)

#drop_duplicates去重方法
#该方法只对DataFrame或者Series类型有效，这种方法不会改变数据的原始排列，并且兼具代码简洁和运行稳定的特点

#使用drop_duplicates方法对菜品名称去重

#对dishes_name去重
dishes_name = detail['dishes_name'].drop_duplicates()
print('drop_duplicates方法去重之后菜品总数为: ',len(dishes_name))

#使用drop_duplicates方法对多列去重
print('去重之前订单详情表的形状为: ',detail.shape)
shapeDet = detail.drop_duplicates(subset = ['order_id','emp_id']).shape
print('依据订单编号，会员编号去重之后订单详情表的形状为: ',shapeDet)

#特征重复
#求出counts和amounts两列数据的kendall法相似度矩阵
#求取销量和售价的相似度

corrDet = detail[['counts','amounts']].corr(method='kendall')
print('销量和售价的kendall法相似度矩阵为: \n',corrDet)

#求出dishes_name ,counts, amounts这3个特征的pearson法相似度矩阵
#对3个特征进行pearson法相似度矩阵的求解，但最终只存在两个特征的相似度矩阵
corrDet1 = detail[['dishes_name','counts','amounts']].corr(method='pearson')
print('菜品名称,销量和售价的pearson法相似度矩阵为: \n',corrDet1)

#通过相似度矩阵去重存在一个弊端,该方法只能对数值型重复特征进行去重，
#类别型特征之间无法通过计算相似系数来衡量相似度，因此无法通过相似度矩阵对其进行去重处理

#使用dataframe.equals方法去重
#定义求取特征是否完全相同的矩阵函数

def FeatureEquals(df):
    dfEquals = pd.DataFrame([],columns=df.columns,index=df.columns)
    for i in df.columns:
        for j in df.columns:
            dfEquals.loc[i,j] = df.loc[:,i].equals(df.loc[:,j])#
    return dfEquals
#应用上述函数
detEquals = FeatureEquals(detail)
print('detail的特征相等的矩阵的前5行5列为：\n',detEquals.iloc[:5,:5])

#通过遍历的方式进行数据筛选
#遍历所有数据
lenDet = detEquals.shape[0]
dupCol = []
for k in range(lenDet):
    for j in range(k+1,lenDet):
        if detEquals.iloc[k,j]&\
        (detEquals.columns[j] not in dupCol): ###???
            dupCol.append(detEquals.columns[j])

#进行去重操作
print('需要删除的列为: ',dupCol)
detail.drop(dupCol,axis=1,inplace=True)
print('删除多余列后detail的特征数目为: ',detail.shape[1])


