import numpy as np#导入NumPy库

#使用sort函数进行直接排序,会改变数组原来的值

np.random.seed(42)#设置随机种子
'''
保证生成随机数的可预测性（即每次生成的随机数相同）
如果不设置seed值，系统会根据时间来选择这个值，此时每次生成的随机数因时间差异
而不同，seed值的有效次数只有一次，若要产生相同的随机数，则每次此都要调用新的随机值,
第二个随机数组生成的值是确定的，但是与第一个不同
'''
arr = np.random.randint(1,10,size = 10)
print(arr)

#对所有元素进行排序
arr.sort()
print(arr)

arr = np.random.randint(1,10,size = (3,3))
print(arr)

#axis = 1时，沿着横轴排序
#arr.sort(axis = 1)
#print(arr)

#axis = 0时，沿着纵轴排序
arr.sort(axis = 0)
print(arr)

#使用argsor和lexsort函数进行间接排序
#使用argsor和lexsort函数，可以在给定一个或多个键（数组）时
#得到一个有整数构成的索引数组，索引值表示数据在新的序列中的位置

#argsort函数，间接排序（不会改变数组原来的值）

arr = np.array([2,3,6,8,0,7])
print(arr)

arr.argsort()
print(arr.argsort())

#lexsort函数（间接联合排序函数）
#可以一次性对多个键（数组）执行间接排序

a = np.array([3,2,6,4,5])
b = np.array([50,30,40,20,10])
c = np.array([400,300,600,100,200])
d = np.lexsort((a,b,c))#lexsort函数只接收一个参数，即（a,b,c)
#多键（数组）排序，是按照最后一个传入数据计算的，通过a,b,对c排序
print("排序后的数组为: ",list(zip(a[d],b[d],c[d])))




