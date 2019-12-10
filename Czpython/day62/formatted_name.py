def get_formatted_name(first_name,last_name):
    """ 返回整洁的姓名"""
    full_name =first_name + ' ' +last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)
#原本只需要写print("Jimi Hendrix"),相比于此，函数更加复杂
#但在需要分别存储大量名和姓的程序中，这样的函数就很有用

#让实参变成可选的，这样使用函数的人只需要在必要的时候才提供额外的信息。可以使用默认值让是擦变成可选的

def get_formatted_nameplus(first_name,last_name,middle_name =''):
    """ 返回整洁的姓名"""
    if middle_name: #如果middle_name不是空字符串 if len(middle_name) != 0
        full_name =first_name + ' ' + middle_name + ' ' +last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_nameplus('jimi','hendrix','Lee')
print(musician)
#在函数定义中首先列出两个形参，中间名是可选的，在函数定以中最后列出该形参，将其默认值设置为空字符串
#可以根据需要进行中间名的指定

#返回字典
#函数可以返回任何类型的值，包括列表，字典等较复杂的数据结构
#例如下面的函数接收姓名的组成部分，并返回一个表示人字典
def bulid_person(first_name,last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first':first_name,'last_name':last_name}
    return person
musician = bulid_person('jimi','hendrix')
print(musician)
#函数bulid_person()接收姓和名,并将这些值封装到字典中。存储first_name的值时，使用的键为'first'，存储last_name的值时使用的键为'last'
#最后返回表示人的整个字典

#这个函数接收简单的文本信息将其放在一个更合适的数据结构里，让你不仅能打印这些信息，还能以其它的方式处理它们
#当前的字符串被标记为名和姓。你可以轻松的扩展这个函数，使其接受可选值，如中间名、年龄、职业、或则要存储的其它信息
#例如下面的修改能够存储年龄
def build_person1(first_name,last_name,age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person1('jimi','hendrix',age='27')  #age = 27也行
print(musician)

#结合使用函数和while循环

def get_formatted_name(first_name,last_name):
    """返回简洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


"""
#这是一个无限循环
while True:
    print("\nPlease tell me your name:")
    print("enter 'q' at any time to quit")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + '!')
"""
#添加一条消息告诉用户如何退出,两个while循环同时调用一个函数，第二个while循环第哦啊用不了函数
while True:
    print("\nPlease tell me your name:")
    print("enter 'q' at any time to quit")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if f_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + '!')

def city_country():
    countryside = input('Please tell me your courtryside')
    nation = input('Please tell me your nation')
    full_name ='"'+countryside +','+nation + '"'
    return full_name
print('\n',city_country())


def make_album(name,album,num=''):
    single = {'name':name,'album':album}
    if num:
        single['num'] = num  #在字典中新加一个key值
    return single
make_album('weiwang','sagou',num=3)
print(make_album('weiwang','sagou',num=3))

while True:
    print("\nenter 'q' at any time to quit")
    name = input('Please input the name of singer')
    if name == 'q':
        break
    album = input('Please input the album')
    if album == 'q':
        break
    make_album(name,album)
    print(make_album(name,album))



