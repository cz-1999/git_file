import numpy as np

#使用mat函数创建矩阵
matr1 = np.mat("1 2 3;4 5 6;7 8 9")#使用分号隔开数据
print(matr1)

#使用matrix函数创建矩阵
matr2 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print(matr2)

#使用bmat函数创建矩阵,分块矩阵，用小矩阵合成大矩阵
arr1 = np.eye(3)
arr2 = np.eye(3)*3
print(np.bmat("arr1 arr2;arr2 arr1"))

#矩阵运算
matr1 = np.mat("1 2 3;4 5 6;7 8 9")
matr2 = matr1*3
print(matr1+matr2)#矩阵相加
print(matr1-matr2)#矩阵相减
print(matr1*matr2)#矩阵相乘

#multiply函数矩阵对应元素相乘
print(np.multiply(matr1,matr2))#矩阵对应元素相乘

#矩阵属性

#矩阵的转置,行变成列，列变成行
print(matr1.T)
#矩阵的共轭转置（实数的共轭是其本身）
print(matr1.H)
#逆矩阵
print(matr1.I)
#返回自身数据的二维数组的一个视图
print(matr1.A)

#ufunc函数（操作对象是数组）
#ufunc函数支持全部的四则运算，比较运算，逻辑运算等，
#数组间的四则运算表示对数组中的每个元素进行运算
#进行四则运算的两个数组的形状必须相同

x = np.array([1,2,3])
y = np.array([4,5,6])

#数组相加
print(x+y)

#数组相减
print(x-y)

#数组相乘
print(x*y)

#数组相除
print(x/y)

#数组幂运算
print(x**y)

#数组的比较运算
'''
ufunc中可以用完整的比较运算:>,<,==,>=,<=,!= 比较运算返回的结果是一个布尔数组
其每个元素为数组对应的比较结果
'''
x = np.array([1,3,5])
y = np.array([2,3,4])

print(x < y)

print(x > y)

print(x <= y)

print(x >= y)

print(x == y)

print(x != y)

#在numpy的逻辑运算中，np.all表示逻辑与，np.any表示逻辑或
print(np.all(x == y))
print(np.any(x == y))

#ufunc函数的广播机制(沿着一个轴进行扩散）

#轴分为横轴和纵轴，对于二维数组 axis = 1 时为横轴 axis = 0时为纵轴，轴的长度对应与维数

#一维数组的广播机制，当用来广播的数组就是一维数组时，则默认沿着0轴（长度为0的轴）广播，
#用来广播的一维数组与另一个数组必须要有一个维度相同

#二维数组的广播机制，用来广播的二维数组与另一个数组必须要有一个维度相同，另一个维度为1，否则会出错

#一维数组广播机制
arr1 = np.array([[0,0,0],[1,1,1],[2,2,2],[3,3,3]])
arr2 = np.array([1,2,3])

print(arr1.shape)

print(arr2.shape)

print(arr1+arr2)

#二维数组的广播机制
arr3 = np.array([[0,0,0],[1,1,1],[2,2,2],[3,3,3]])

arr4 = np.array([1,2,3,4]).reshape((4,1))

print(arr3+arr4)








