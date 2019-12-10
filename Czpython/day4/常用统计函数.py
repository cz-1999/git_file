import numpy as np
arr = np.arange(20).reshape(4,5)
print(arr)

#sum函数
#计算数组和
print(np.sum(arr))
#沿y轴计算数组和
print(arr.sum(axis = 0))
#沿x轴计算数组和
print(arr.sum(axis = 1))

#mean函数
#计算数组均值
print(np.mean(arr))
#沿y轴计算数组均值
print(arr.mean(axis = 0))
#沿x轴计算数组均值
print(arr.mean(axis = 1))

#std函数
#计算数组标准差
print(np.std(arr))

#var函数
#计算数组方差
print(np.var(arr))

#min函数和max函数
#计算数组最大值
print(np.max(arr))
#计算数组最小值
print(np.min(arr))

#argmin函数 和 argmax函数
#返回数组最大元素索引
print(np.argmax(arr))
#返回数组最小元素索引
print(np.argmin(arr))

#以上函数均采用聚合计算直接产生最后结果

#cumsum函数和cumprod函数 采用不聚合计算 产生一个有中间结果组成的数组
arr = np.arange(2,10)
print(arr)
#元素累计和
print(np.cumsum(arr))
#元素累计积
print(np.cumprod(arr))