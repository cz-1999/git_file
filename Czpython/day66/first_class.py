#面向对象编程是最有效的软件编写方法之一,在面向对象编程时你将编写表示现实世界中的事物和情景的类，并基于这些类来创建对象
#编写类时，你定义一大类对象都有的通用行为。基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性
#跟据类来创建对象被称为实例化，这让你能够使用类的实例


#创建Dog类
#根据Dog类创建的每个示例都将存储名字和年龄。我们赋予了每条小狗蹲下(sit())和打滚(roll_over())的能力
class Dog():
    """一次模拟小狗的简单尝试"""   #文档字符串  对类的功能做了描述

    def __init__(self,name,age):
        """初始化属性name 和 age"""
        self.name = name   #以self为前缀的变量可供类中的所有方法使用，像这样可通过实例访问的变量成为属性
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + "is now sitting")

    def roll__over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+"rolled over!")


#我们定义了一个类,在python中,首字母大写的名称指的是类，，这个类定义中的括号是空的，因此我们要从空白创建这个类
'''
1.方法__init__()
类中的函数称为方法:前面学的有关函数的一切都适用于方法，就目前而言，唯一重要的差别是调用方法的方式。__init__是一个特殊的方法，每当你根据Dog类
创建新的示例是python都会自动运行它，在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定,旨在避免python默认方法与普通方法发生名称冲突

我们将方法__init__()定义称包含三个形参:self,name,age 在这个方法的定义中，形参self必不可少,还必须位于其它形参的前面。为何必须在方法定义中
包含形参self呢？




'''

#根据类创建实例,__init__()并未显示的包含return语句,但python自动返回一个表示这条小狗的实例，我们将这实例存储在变量my_dog里,在这里命名的约定很有用
my_dog = Dog('weiwang',6)  #我们通常可以认为首字母大写的名称（如Dog）指的是类，而小写的名称（如my_dog）指的是根据类创建的实例

#访问属性
#要访问实例的属性可使用据点表示法
print("My dog's name is "+my_dog.name.title() + ".")
print("My dog is "+str(my_dog.age)+" years old.")

#调用方法
#根据Dog类创建实例后，就可以使用据点表示法来调用Dog类中定义的任何方法
my_dog.sit()
my_dog.roll__over()

#这种语法很有用，如果给属性和方法指定了合适的描述星名称，如name,age,sit(),roll_over(),即便是从未见过的代码块，我们也能轻松推断出它是什么

#创建多个实例
my_dog = Dog('weiwang',6)
your_dog = Dog('cunlin',3)
print("My dog's name is "+my_dog.name.title() + ".")
print("My dog is "+str(my_dog.age)+" years old.")
print("Your dog's name is "+your_dog.name.title() + ".")
print("Your dog is "+str(your_dog.age)+" years old.")
#可以按需求根据一个类创建任意数量的实例，条件是将每个实例都存储在不同的变量中，或占用列表或字典的不同位置

class Restaurant():
    """一次模拟餐馆的简单尝试"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restauranr(self):
        print("The restaurant's name is " + self.restaurant_name + " restaurant. Its type is " + self.cuisine_type )

    def open_restaurant(self):
        print("The restaurant is opening")

my_restaurant = Restaurant('cz','xican')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restauranr()
my_restaurant.open_restaurant()
your_restaurant = Restaurant('weiwang','zhongcan')
their_restaurant = Restaurant('zhenwei','xican')
your_restaurant .describe_restauranr()
their_restaurant.describe_restauranr()

class User():
    """一次模拟用户的简单尝试"""
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet_user(self):
        print("Hello " + self.first_name.title() + self.last_name.title() + " Nice to meet you!")

user1 = User("li","weiwang")
user2 = User('cheng','zhang')
user1.greet_user()
user2.greet_user()
