import numpy as np

iris_speal_length = np.loadtxt("D:/python/czpython/iris_sepal_length.csv"
 ,delimiter = ",")#数组名要检查好，读取文件
print('花萼长度表为：',iris_speal_length)
iris_speal_length.sort()#对数据进行排序
print('排序后的花萼长度表为：',iris_speal_length)

#去除重复值
print('去重后的',np.uinque(iris_speal_length))
print('花萼长度表的总和为:',np.sum(iris_speal_length))#计算数组总和
print('花萼长度表的均值为:',np.mean(iris_speal_length))#计算数组均值
print('花萼长度表的标准差为:',np.std(iris_speal_length))#计算数组的标准差
print('花萼长度表的房产为:',np.var(iris_speal_length))#计算数组的方差
print('花萼长度表的最小值为:',np.min(iris_speal_length))#计算数组的最小值
print('花萼长度表的最大值为:',np.max(iris_speal_length))#计算数组的最大值
