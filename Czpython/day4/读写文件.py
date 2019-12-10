import numpy as np#导入NumPy库

#二进制数据存储
arr = np.arange(100).reshape(10,10) #创建一个二维数组

#单个数组存储(两个参数：fname:文件名 ,数组名）
np.save("D:\python\czpython\save_arr",arr)#保存数组
print("保存的数组为:",arr)

#多个数组存储
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.arange(0,1.0,0.1)
np.savez("D:\python\czpython\savez_arr",arr1,arr2)#把数组arr1和数组arr2存到一个文件里面去
print(arr1)
print(arr2)

#二进制文件读取

#load函数（以文件名做参数）

#读取含有单个数组的文件
loaded_data = np.load("D:\python\czpython\save_arr.npy")
print("读取的数组为:",loaded_data)

#读取含有多个数组的文件
loaded_data1 = np.load("D:\python\czpython\savez_arr.npz")#文件名要写对
print("读取的数组为:",loaded_data1["arr_0"])#读取多个文件时必须从0开始计数，往后延伸
print("读取的数组为:",loaded_data1["arr_1"])

#保存多个文件时，提取的数组名是什么？
'''
#savetxt函数（四个参数）
arr = np.arange(0,12,0.5).reshape(4,-1)#-1的意思是数组会根据剩下的维度计算出另一个维度的值
#fmt = "%d"表示保存为整数
np.savetxt("D:\python\czpython\savetxt_arr.txt",arr,fmt= "%d",delimiter = ",")
#读入的时候需要用指定逗号分隔

#loadtxt函数两个参数（fname：文件名，delimiter:分隔符）
loaded_data = np.loadtxt("D:\python\czpython\savetxt_arr.txt",delimiter = ",")
print(loaded_data)

#genfromtxt函数和loadtxt函数相似，它面向结构化数组和缺失数据(三个参数）
loaded_data = np.genfromtxt("D:\python\czpython\savetxt_arr.txt",delimiter = ",")
print(loaded_data)
'''