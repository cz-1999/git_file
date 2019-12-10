#列表由一系列按特定顺序排列的元素组成，在python中用方括号[]来表示列表，并用逗号分隔其中的元素
bicycles = ['trek','cannondale','readline','specialized']
#python将打印列表的内部表示，包括方括号
print(bicycles)
#访问列表元素
#列表是有序的集合，因此要访问列表的任何元素，只需将该元素的位置或者索引告诉python即可，要访问列表元素可指出列表的名称再指出元素的索引，并将其放到方括号内
print(bicycles[0])
#当请求获得列表元素时，python只返回该元素而不包括方括号和引号

#可以调用第二章的title()方法让元素'trek'的格式更整洁:
print(bicycles[0].title())

#索引从0而不是1开始
#在python中第一个列表元素的索引为0，而不是1.大多数编程语言都是如此，这与列表操作的底层实现相关，要访问列表中的任意元素都可将其位置减1并将结果作为索引
print(bicycles[1])
print(bicycles[3])
#python为访问最后一个列表元素提供了一种特殊语法，通常将索引指定为-1，可让python返回最后一个列表元素
print(bicycles[-1])
#这种语法很有用，因为你经常需要在不知道列表长度的情况下访问最后的元素，这种约定也使用与其它负数索引，例如，索引-2返回倒数第二个列表元素

#使用列表中的各个值
#可想使用其它变量一样使用列表中的各个值，例如你可以使用拼接根据列表中的值来创建消息
message = 'My first bicycle was a ' + bicycles[0].title() + '.'
print(message)
names = ['wei wang','zhen wei','li hao']
for i in names:
    message ='Hello ' +i.title() +'!'
    print(message)
message = 'I would like to own a ' +bicycles[0]
print(message)

#修改、添加和删除元素
#你创建的大多数列表都是动态的，将随着程序的运行增删元素

#修改列表元素，要修改列表元素可指定列表名和要修改的元素的索引，在指定该元素的新值
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]= 'ducati'
print(motorcycles)
#你可以修改任何列表元素的值，而不仅仅是第一个元素的值

#在列表中添加新元素，出于众多原因，例如你可能希望游戏中出现新的外星人，添加可视化数据或给网站添加新注册的用户，python提供了多种在既有列表中添加新数据的方式

#在列表末尾添加元素，最简单的方式是将元素附加到列表末尾
print(motorcycles)
motorcycles.append('ducai')
print(motorcycles.append('ducai'))#这样输出值为none
print(motorcycles)
#方法append()将元素'dutai'添加到了列表末尾，而不影响列表中的其它所有元素

#方法append()让动态的创建列表易如反掌，例如，你可以先创建一个空列表，再使用一系列append语句添加元素
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
#最终列表与前述示例中的列表完全相同
print(motorcycles)
#这种创建列表的方式极其常见，因为经常要等程序运行后，你才知道用户要在程序中存储哪些数据。
# 为了控制用户可首先创建一个空列表，用于存储用户将要输入的值然后将用户提供的每个新值附加到列表中

#再列表中插入元素
#使用方法insert()可在列表的任何位置添加新元素。为此你需要指定新元素的索引和值