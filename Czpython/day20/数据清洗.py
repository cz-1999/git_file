import pandas as pd
#检测预处理重复值
#类型重复，菜品订单详情表中dishes_name中存放了每个订单的菜品，要找出所有已点菜品，最简单的方法就是利用去重实现

# 1. list去重，对某一列去重
#利用list构建的函数去重，代码冗余，但是不会改变内部数据的顺序
detail = pd.read_csv('D:/python/czpython/detail.csv') #pd.read_csv数据读取函数，以dataframe的形式存入内存
#dataframe相当于内存中的数据库
def delRep(list1):
    list2 = []        #建立一个空列表
    for i in list1:           #遍历list1 将不重复的数据存入 list2
        if i not in list2:
            list2.append(i)   #append() 函数,往列表中追加数据
    return list2
# delRep函数的对象是列表
#利用list函数可以把 dataframe列中的数据提取出来，构建成一个列表
dishes = list(detail['dishes_name'])
dish = delRep(dishes) #去重后的数据

# 2. 利用(集合)set的特性去重，集合具有元素唯一性，set的对象也是列表
#set内具有元素唯一性,但是会改变数据的排列顺序
dish_set = set(dishes)

#利用drop_duplicates方法对菜名进行去重
#该方法只对DataFrame或者Series类型有效，不会改变数据的原始排列，且代码简洁，运行稳定

