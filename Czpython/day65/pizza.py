#有时候你预先不知道需要接受都少个实参，好在python允许函数从调用语句中收集任意数量的实参，例如制作比萨的函数，它需要接受很多配料，但你无法预料顾客
#要多少中配料。下面函数中的形参*toppings，不管调用语句提供多少实参这个形参都将它们统统收入囊中
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
#形参名*toppings中的星号让python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中，函数体内的print语句通过生成输出来证明python
#能够处理一个值调用的情形，也能处理三个值调用的情形，它以类似的方式处理不同的调用，注意，python将实参封装到一个元组中，即便函数只收到一个值也如此

#现在将这条print语句替换为一个循环，对配料列表进行遍历，并对顾客点的比萨进行描述
def make_pizzaplus(*toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a pizza with the followings")
    for topping in toppings:
        print("-" + topping)

make_pizzaplus('pepperoni')
make_pizzaplus('mushrooms','green peppers','extra cheese')

#不管函数收到的实参有多少个这种语法都管用

#结合使用位置实参和任意数量的实参
#如果要让函数接受不同类型的实参，必须在函数定义里将接纳任意数量实参的形参放到最后
#python先匹配位置实参和关键字实参，再将剩下的实参都收集到最后一个形参里，例如还需要李哥表示比萨尺寸的实参，
#必须将该形参放到形参*toppings的前面
def make_pizzaplus1(size,*toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a " +str(size) + "-inch pizza with the followings:")
    for topping in toppings:
        print("-" + topping)


make_pizzaplus1(16,'pepperoni')
make_pizzaplus1(12,'mushrooms','green peppers','extra cheese')

#基于上述函数的定义，python将收到的第一个值存储在形参size中，并将其它所有值都存储在元组toppings中。在函数调用中，首先指定表示比萨尺寸的实参
#，然后根据需要指定任意数量的配料

#使用任意数量的关键字实参
#有时候，函数需要接受任意数量的实参，但预先不知道串第给函数的是什么信息，
# 在这种情况下，可将函数编写成能接受任意数量的键—值对--调用语句提供了多少就接受多少

#例如，创建用户简介；你知道你将收到关于用户的信息，但不知道是什么信息，在下面这个示例中函数将接受名和形，同时还接受任意数量的关键字实参

def build_profile(first,last,**user_info):
    """创建一个字典其中包含我们知道的有关用户的一切信息"""
    profile={}
    profile['first_name'] = first #在字典中创建first_name键并为其赋值
    profile['last_name'] = last
    for key,value in user_info.items():  #items()方法将字典中的键值对先存到元组中再将元组存到列表中，循环列表中的元组，将元组中的值赋给key和 value
        profile[key] = value
    return profile
user_profile = build_profile('alert','einstein',location='princeton',field='physics')
print(user_profile)

#形参**user_info中的两个星号让python创建一个名为user_info的空字典，并将收到的所有键值对都封装道这个字典中
a = {'first_name': 'alert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}
print(a.items())

def make_sandwich(*foods):
    """打印顾客的所有配料"""
    print("\nMaking a sandwich with the followings")
    for food in foods:
        print(food)
make_sandwich('tomato','potato','ham')

user_profile_cz = build_profile('程','长',school='haut',grade='1')
print(user_profile_cz)

def make_car(manufacturer,model,**car_other):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key,value in car_other.items():
        car[key] = value
    return car
the_car = make_car('subaru','outback',color='blue',tow_package=True)
print(the_car)

#将函数存储在模块中
"""
函数的优点之一是使用它们可将代码块与主程序分离，通过给函数指定描述性的名称，可让主程序容易理解许多。你还可以进一步将函数存储在被称为模块
的独立文件中，再将模块导入到主程序中，import语句允许当前运行的程序文件中使用模块中的代码

通过将函数存储在独立的文件中，可隐藏代码的细节，将重点放在程序的高层逻辑上。这还能让你在众多不同的程序中重用函数。将函数存储在独立文件中后
可与其它程序员共享这些文件而不是整个程序，知道如何导入函数能让你使用其它程序员编写的函数
"""

