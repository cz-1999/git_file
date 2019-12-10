#仅当列表为空时，访问最后一个元素的方式会导致错误
motorcycles = []

#列表中不包含任何元素所以，python返回一条索引错误的消息
#print(motorcycles[-1])
print(len(motorcycles))

#循环遍历列表
magicians = ['alice','davaid','carolina']
for magician in magicians:
    print(magician)
#这行代码让python从列表中取出一个名字，并将其存储在变量magician中，最后我们让python打印前面存储到变量magician中的名字，pyhon将重复执行代码行

#深入的研究循环

#for magician in magicians:
#这行代码让python获取列表magicians中的第一个值，并将其存储到变量magician中，接下来python读取下一行代码，

#print(magician)
#它让python打印magician的值--依然是'alice',监狱该列表还包含其它的值，python返回到循环的第一行:
#python将后面的连个值打印出来，程序结束

'''
刚开始写循环时，对列表中的每个元素，都将执行循环指定的步骤，而不管列表包含多少个元素，列表包含多少个元素就执行多少次
另外，写for循环时，对于存储列表中每个值的临时变量，可指定任何名称，然而，选择描述单个列表元素的有意义的名称右很大帮助
例如
for cat in cats
for dog in dogs
for item in list_of_items
'''

#在for循环中执行更多的操作
