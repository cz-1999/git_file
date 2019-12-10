import numpy as np

#生成随机数组
print("生成随机数组:",np.random.random(100))
#每次运行生成的随机数组都不一样
print(np.random.random(100).ndim)
#生成100个随机元素的一维数组

#生成服从均匀分布随机数组
print(np.random.rand(10,5))

#生成服从正态分布随机数组
print(np.random.randn(10,5))

#生成给定上下限范围的随机数组
print(np.random.randint(2,10,size = [2,5]))







