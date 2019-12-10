import numpy as np

#数据类型转换
print(np.float64(42))
print(np.int64(42.0))
print(np.bool(42))
print(np.bool(0))
print(np.float(True))
print(np.float64(False))

#创建数据类型
df = np.dtype([("name",np.str_, 40),("numitems",np.int64),("price",np.float64)])
print("数据类型为:",df)

#查看数据类型
print("数据类型为:",df["name"])
print("数据类型为:",np.dtype(df["name"]))

#自定义数组类型
itemz = np.array([("tomatoes",42,4.14),("cabbages",13,1.72)],dtype = df)
print("自定义数组为",itemz)
