import copy
name = "wangshengrong jicunlin lihao liweiwang"
print(name)
name = ["wangshengrong","jicunlin",["lihao","chengzhang"],"liweiwang"]#列表
'''
print(name)
print(name[-4])#单取某一个值
print(name[-1])#取最后一个值
print(name[0:2])#切片 顾头不顾尾
name[:]#完全切片
print(name[-3:-1])#切片 从左往右取
print(name[:3])#前面的不写默认从0开始取
print(name[2:])#后面的不写默认取到最后一个
'''
'''
name.append("wangzhenwei")#往后追加一个
name.insert(1,"chengzhang")#插入 写要插入的地方和名字
print(name.index("chengzhang"))#找出元素的脚码
name.reverse()#逆置列表
'''
'''
#names2 = copy.deepcopy(name)#深copy
#names2 = copy.copy(name)  ==  names2.copy(name)#浅copy
name[0] = "汪生荣"
name[2][0]="李浩"
name3=[1,2,3]
#print(names2)
#print(name)
print(name.count("lihao"))#元素的数量
print(name)
#print(name[0:-1:2])#列表切片
#print(name[::])#默认为从第一个到最后一个步长为1
#for i in name:#列表的遍历
    #print(i)
#name.extend(name3)#字符串拼接
'''
'''
del name3 #变量删除
name.clear() #清空
name.remove("汪生荣")#删除某个人
del name[0]
name.pop()#默认删除最后一个
name.pop(0) == del name[0]
name.sort()#列表排序
'''
#print(name)
name = ("liweiwang","wangzhenwei","baoyvjia","lixingang")#元组就是只读列表，
# 不能改变，只能切片，和查找某个元素的位置
print(name)
