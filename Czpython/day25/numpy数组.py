#NumPy数组是用于科学计算的模块，
# 可以完成科学计算的任务，
# 可以被用作高效的多维数据容器
# 可以保存任意类型的数据
# 可以无缝整合各种数据

#python提供了一个array模块，array和list不同(感觉几乎一样，还是有差别)，它直接保存数值，和C语言的一位数组比较类似，但是python的array模块
#不支持多维，也没有各种运算函数，因此不适合做数值运算，numpy弥补了这些不足，numpy提供了存储单一数据类型的多维数组-ndarray

#numpy提供了两种基本的对象: ndarray(N-dimensional Array Object) 和 ufunc(Universal Function Object)
#ndarray(数组)是存储单一数据类型的多维数组，ufunc则是能够对数组进行处理的函数

#ndarray数组属性
#ndim 返回int,表示数组的维数
#shape 返回tuple(元组) 表示数组的尺寸,对于n行m列的矩阵,形状为(n,m)
#size 返回int 表示数组元素总数，等于数组形状的乘积
#dtype 返回data-type描述数组中元素的类型  ndarray数组存储单一数据类型,所以是dtype 而不是dtypes
#itemsize 返回 int 表示数组的每个元素的大小(以字节为单位),例如，一个元素类型为float64的数组的itemsize属性值为8
# (float64占用64个bits,每个字节长度为8，所以64/8,占用8个字节,又如，一个元素类型为complex32的数组的itemsize属性值为4，即32/8)

#创建数组
#numpy提供了array函数可以创建一维或多维数组
#主要参数 object: 接收 array 表示想要创建的数组。无默认
#dtype : 接收data-type 表示数组所需的数据类型。如果未给定，则选择保存对象所需的最小类型
#ndmin : 接收int 指定数组应该具有的最小维度数。默认为none,     指定生成数组的维度
#arr = np.array([ 1,1,1],dtype= int64, ndmin =4)

import numpy as np
#一维数组
arr3 = np.array([1,2,3,4])
print(arr3)
#多维数组
arr1 = np.array([1,2,3,4],dtype='int64',ndmin=5)
print(arr1)
print(arr1.dtype)
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9],[11,12,13]])
print(arr2)
print(arr2.dtype)

#查看数组属性
print(arr2.ndim,arr2.shape,arr2.size,arr2.dtype,arr2.itemsize)

#重置数组的shape属性

#1,用数组的shape属性改，直接在原数组上改
#arr2.shape = 4,3
print(arr2)
#2,用reshape()函数改 arr.reshape(4,3),需要创建一个新的数组
arr2 = arr2.reshape(3,4)
print(arr2)
#Python中有四种内建的数据结构，即列表、元组、字典、集合。其实都属于——序列。
#上面的例子都是先创建一个python序列，然后在通过array函数将其转化为数组,这样效率不高，python提供了专门用来创建数组的函数
#arange函数，arange函数类似于python自带的函数range,通过指定开始值，终值，步长来创建   '一维数组' ，创建的数组不含终值
# arr = np.arange(开始值，终值，步长)

print(np.arange(0,1,0.2))

#linspace函数通过指定开始值,终值和元素个数来创建一位数组,                arr = np.linspace(开始值，终值，元素个数)
print(np.linspace(0,1,12))   #元素个数为12，即包括0,1 一共有12个元素，0和1之间还要有10个数插入，这10个数把1分成11份，即每一份的长度为1/11

#logspace函数,与linspace函数类似,它创建的是等比数列。例如,生成1(10**0) ~100(10**2)的20个元素的等比数列
print(np.logspace(0,2,20)) #20个元素，除了1和100外,还有18个元素，把1-100之间分成19份,等比系数 q的19次方等于100

#numpy还提供了其它函数来创建特殊数组,如zeros,eye,diag,ones等
#zeros函数用来创建全0数组,即创建数组的值全部填充为0，zeros函数的参数为tuple(元组),arr = np.zeors((2,3))
print(np.zeros((2,3)))
#ones函数与zeors函数类似
# 用来创建全1数组,即创建数组的值全部填充为1，ones函数的参数为tuple(元组),arr = np.ones((2,3))
print(np.ones((2,3)))
#eye函数用来生成主对角线上元素为1，其它的元素为0的数组，类似单位矩阵，参数为int  arr = np.eye(n）
print(np.eye(3))
#diag函数用来创建类似对角的数组,即除对角线以外的其它元素都为0，对角线上的元素可以是0或其它值,参数为array arr = npp.diag([1,2,3,4])
print(np.diag([1,2,3,4]))

#数组数据类型
#为了更精确的计算结果，需要使用不同精度的数据类型，numpy极大的扩充了原生的python数据类型
#其中大部分数据类型是是以数字结尾的，这个数字表示其在内存中占有的位数
#在numpy数组中，所有元素类型必须是一致的，这样做的好处是更容易确定数组索需要的存储空间
#bool 用一位存储的布尔类型（值为True或False)
#inti 有所在的平台决定其精度的整数(一般为int32或int64)
#int8 整数,范围为-128(-2**7)--127(2**7-1)  一个bite表示符号  int16 int32 int64
#uint8 无符号整数0--（2**8-1）  uint16 uint32 uint64
#float16 半精度浮点数(16位),其中1位表示正负号，用5位表示指数，用10位表尾数
#float32 单精度浮点数(16位),其中1位表示正负号，用5位表示指数，用10位表尾数
#float64或float 双精度浮点数(16位),其中1位表示正负号，用5位表示指数，用10位表尾数
#complex64 复数，分别用两个32位浮点数表示实部和虚部
#complex128或complex 复数，分别用两个64位浮点数表示实部和虚部

#数组类型转换
#np.float()  np.int64()  np.bool
print('整型转浮点型:',np.float(42))
print('浮点型转整型:',np.int8(32.0))
#0转布尔型为True，非0转布尔型均为True
print('整形转布尔型:',np.bool(42))
print('整形转布尔型:',np.bool(0))
print('布尔型转浮点型:',np.float(True))
print('布尔型转浮点型:',np.float(False))

#创建数据类型来存储数据，类似于C中的结构体，df = np.dtype([(    ),(     ),(     )])
df = np.dtype([('name',np.str_,40),('numitems',np.int64),('price',np.float64)])
print(df)

#查看数据类型,可直接查看，或者使用np.dtype函数查看
print(df['name'])
print(np.dtype(df['name']))

#使用array创建数组时，数组的数据类型默认是浮点型，自定义数组类型，可以预先指定数据类型
itemz = np.array([('tomatoes',42,4.14),('cabbages',13,1.72)],dtype=df)
print(itemz)
#生成随机数组
#numpy提供了生成随机数的功能，真正的随机数很难获得，实际中大部分使用的是伪随机数，通过复杂函数生成，但是伪随机数就能满足大部分需求
#一些特殊情况除外，如进行高精度的模拟实验
#numpy中random模块，包括了可以生成服从多种概率分布的随机函数

#np.random.random(n)函数,生成n个随机数
print(np.random.random(100))

#np.random.rand(10,5) 可以选择生成随机数的行和列,生成服从均匀分布的随机数
print(np.random.rand(10,5))

#np.random.randn(10,5) 可以选择生成随机数的行和列,生成服从正态分布的随机数
print(np.random.randn(10,5))

#以上代码每次运行后生成的随机数组都不一样,seed 确定随机数生成的种子,seed相同，生成的随机数组相同 可以通 np.random.seed()
#设置随机种子，随机种子只对最邻近的随机数组生效，要想获得相同的随机数组需设置多个相同的随机种子
np.random.seed(42)
#np.random.randint(2,10,size=[2,5]) 可以生成给定上下限范围的随机数 size可以决定生成数组的形状
print(np.random.randint(2,10,size=[2,5]))
#random模块的常用随机数生成函数
#seed 确定随机数生成起的种子
#permutation 返回一个序列的随机排序或返回一个随机排列的范围
#Shuffle 对一个序列进行随机排序
#binomial 产生二项分分布的随机数
#normal 产生正态（高斯）分布的随机数
#beta 产生beta分布的随机数
#chisquare 产生卡方分布的随机数
#gamma 产生gamma分布的随机数
#uniform 产生在[0,1]中均匀分布的随机数

#通过索引访问数组
arr = np.arange(10)
#用整数作为下标可以获取数组中的某个元素
print(arr[5])

#用范围作为下标获取数组的一个切片,包括arr[3],不包括arr[5]
print(arr[3:5])

#省略开始下标表示从arr[0]开始
print(arr[:5])

#下标可以使用负数，-1表示从数组最后往前数的第一个元素
print(arr[-1])

#下标可以用来修改元素的值
arr[2:4]=100,101
print(arr)

#范围中第3个参数表示步长,2表示隔一个元素去一个元素     arr[a:b:c]
print(arr[1:-1:2])

#步长为负数时，开始下标必须大于结束下标
print(arr[5:1:-2])

#多维数组索引
#多维数组每个维度之间都有一个索引，各个维度的索引之间用隔开
arr = np.array([[1,2,3,4,5],[4,5,6,7,8],[7,8,9,10,11]])
#索引第0行，第3列和第4列元素
print(arr[0,3:5])
#索引第1行和第2行中第2-4列元素
print(arr[1:,2:])
#索引第二列元素
print(arr[:,2])
#使用整数函数和布尔值索引来访问多维数组
#从两个序列的对应位置取出两个整数来组成下标     arr[ (   ),(   ) ]
print(arr[(0,1,2),(1,2,3)])
#索引第1，2行中的第0，2，3列的元素
print(arr[1:,(0,2,3)])
#mask是一个布尔数组，会对布尔值为1的进行索引
mask = np.array([1,0,1],dtype=bool)
#索引第0，2行中的第2列元素
print(arr[mask,2])

#变换数组形态
#对数组进行操作要改变数组维度，numpy中常用 reshape函数来改变数组维度，其参数是正整数元组，分别指定数组在每个维度上的大小
#reshape函数在改变原始形状的同时不改变原始数据的值，如果指定的维度和数组的元素数目不吻合，则函数将抛出异常
arr = np.arange(12)
print(arr)
print(arr.reshape(3,4))
print(arr.reshape(3,4).ndim)

#在numpy中可以使用ravel函数完成数组展平工作(横向展平),ravel函数在改变原始形状的同时不改变原始数据的值,
arr1 = arr.reshape(3,4)
print(arr1)
print(arr.ravel())
