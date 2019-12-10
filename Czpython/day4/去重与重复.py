import numpy as np
arr = np.array(['小明','小黄','小花','小明','小花','小兰','小白'])

#unique函数，找出数组中得唯一值并返回一排序结果
#print(np.unique(arr))

#与unique等价的代码
print(sorted(set(arr)))#set具有元素唯一性

arr2 = np.array([1,1,1,2,2,2,3,3,3,4,4,5,6,7,8,9])

#print(np.unique(arr2))
print(sorted(set(arr2)))#sorted函数，原列表数据不改变返回一个新列表

#利用tile函数和repeat函数实现数据重复

#tile函数
#np.tile(A,reps),参数A指定重复的数组，reps指定重复的次数
arr = np.arange(5)
print(arr)
print(np.tile(arr,3))

#ctrl+鼠标左键可以在右侧行数上标记对勾

#repeat函数
#np.repeat(a,repeats,axis = None) 参数a指重复的数组元素，参数repeats重复次数
#参数axis指沿着那个轴重复
np.random.seed(42)
arr = np.random.randint(0,10,size = (3,3))
print(arr)

#对每个元素沿列进行重复
#print(arr.repeat(2,axis = 0))

#对每个元素沿行进行重复
print(arr.repeat(2,axis = 1))

#tile和repeat的区别是，tile函数是对数组进行重复操作，
# repeat函数是对数组中的每个元素进行重复操作