import numpy as np #导入numpy库
arr1 = np.array([1,2,3,4])#创建一维数组
print("创建的数组为:",arr1)

arr2 = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])#创建二维数组
print("创建的数组为:",arr2)

print("数组维数:",arr2.ndim,arr1.ndim) #表示数组维数

print("数组维度:",arr2.shape,arr1.shape) #表示数组维度

print("元素总数:",arr2.size,arr1.size) #表示数组元素总数

print("数组类型:",arr2.dtype,arr1.dtype) #表示数组类型

print("数组类型:",arr2.itemsize,arr1.itemsize) #表示数组每个元素的大小

arr2.shape = 4,3 #重新设置shape
print("重置后的shape为：",arr2)

print("使用arange函数创建数组为：",np.arange(0,1,0.1))#通过指定开始值，终值，步长，
# 创建的数组不包括终值

print("使用linspace函数创建的数组为: ",np.linspace(0,1,12))#需要设定初始值，终值，
# 和元素个数，按等差数列来创建
print("使用logspace函数创建的数组为: ",np.logspace(0,1,12))#需要设定初始值，终值，
# 和元素个数，按等比数列来创建

#其它函数来创建特殊数组

#zeros函数：创建值全部为0的数组，以元组为基础
print(np.zeros((2,3)))

#ones函数创建元素全为1的数组，以元组为基础
print(np.ones((5,3)))

#eye函数：创建主对角线为1，其他元素为0的元素
print(np.eye(3))

#diag函数创建类似对角的数组，除对角线意外的其它元素都为0，
# 对角线上的元素可以是0 或是其他值
print(np.diag([1,2,3,4]))#以列表为基础
#自动把元素放到对角线上，有几个元素就有几行几列













