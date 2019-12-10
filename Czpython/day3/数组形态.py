import numpy as np
arr = np.arange(12)
print(arr)

#用数组的属性改变数组形态
arr.shape = 4,3
print(arr)

#用reshape函数改变数组形态，参数为正整数元组
print(arr.reshape(3,4))

#查看数组维度
print(arr.reshape(3,4).ndim)

#使用ravel函数展平数组,横向展平
arr = np.arange(12).reshape(3,4)
print(arr)
#print(arr.ravel())

#使用flatten函数展平数组,可选择横向展平或者纵向展平
#print(arr.flatten())#横向展平
print(arr.flatten("F"))#纵向展平

#数组结合以元组的方式结合
arr1 = np.arange(12).reshape(3,4)
arr2 = arr1*3
'''
hstack 函数横向结合
print(np.hstack((arr1,arr2)))
横向结合，两个数组按照顺序横着放

vstack 函数纵向结合
print(np.vstack((arr1,arr2)))
纵向结合，两个数组按照顺序竖着放
'''
'''
#concatenate函数 横纵向结合
#print(np.concatenate((arr1,arr2),axis = 1))#横向结合
print(np.concatenate((arr1,arr2),axis = 0))#纵向结合
'''

#数组分割，直接代入参数分割
arr1 = np.arange(12).reshape(3,4)
arr2 = arr1*3

#hsplit 函数横向分割
print(np.hsplit(arr1,2))
#横向分割，数组分向两边

#vstack 函数纵向分割
#print(np.vsplit(arr1,2))
#纵向分割，数组分向上下

#split函数 横纵向分割
#print(np.split(arr1,2,axis = 1))#横向分割
#print(np.split(arr1,2,axis = 0))#纵向分割

