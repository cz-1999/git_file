#打印问候语的简单函数
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
greet_user()
#使用关键字 def来告诉python，你要定义一个函数。这是函数定义，向python指出函数名，还能再括号内指出python为完成任务，需要什么样的信息
#在这里,函数名为greet_user(),它不需要任何信息就能完成工作，因此括号是空的（即便如此，括号也必不可少）。最后定义以冒号结尾
#冒号后面的所有缩进，构成了函数体，"""显示简单的问候语 """是被称为文档字符串的注释，描述了函数是做什么的。
# 文档字符串用三引号括起,python使用它们来生成有关程序中函数的文档

#要使用这个函数可调用它，函数调用让python执行函数的代码。要调用函数可依次指定函数名以及用括号括起的必要信息

#向函数传递信息
#可在函数定义def greet_user()的括号内添加username。通过再这里添加username,
# 就可让函数接收username指定的任何值。现在这个函数要求你调用它时给username指定一个值

def greet_user1(username):
    """显示简单的问候语"""
    print("Hello, " +username.title() +"!")
greet_user1('jesse')
greet_user1('weiwang')
greet_user1('zhenwei')

#实参和形参
#前面定义函数时，要求给变量username指定一个值，调用这种函数并提供这种信息时，它会打印相应的问候语。
#在函数的定义中,变量username是一个形参--函数完成工作所需要的一项信息，在代码中值'jesse'是一个实参，实参是调用函数是传递给函数的信息。
#我们调用函数是，将要让函数使用的信息放到括号内。将实参的值传递给函数，这个值被存储在形参username中


def display_message():
    print('sa gou wei wang')
display_message()
def favorite_book(title):
    print('One of my favorite books is ' + title.title() +'.' )
favorite_book('alice in wonderland')

#传递实参
#位置实参，调用函数时，python必须将函数调用中的每个实参都关联到函数定义中的一个形参，
# 最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\n I have a " + animal_type + ".")
    print("My" + animal_type + "'s name is" + pet_name.title() + ".")
describe_pet('hamster','harry')
#调用函数是需要按顺序提供一种动物类型和一个名字
#调用函数数次，可以根据需要调用函数任意次，要在描述一个宠物，只需再次调用describe_pet()即可
#在函数中可以使用任意数量的位置实参，python将按顺序将函数调用中的实参关联到函数定义中相应的形参

#位置实参的顺序很重要，
describe_pet('harry','hamster')

#关键字实参
#在函数调用时，我们向python明确指出各个实参对应的形参，关键字实参的顺序无关紧要，python知道各个值应该要存储到那个形参了
describe_pet(animal_type='hamster',pet_name='harry')
#使用关键字实参时，务必准却的指定函数定义中的形参名

#默认值
#在编写函数时可以给每个形参指定默认值,在函数调用时给形参提供实参时，python将使用指定的实参值，否则使用形参的默认值。因此
#给形参指定默认值后可在函数调用中省略相应的实参
def describe_pet(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print("\n I have a " + animal_type + ".")
    print("My" + animal_type + "'s name is" + pet_name.title() + ".")
describe_pet('harry')

#在函数的定义中修改了形参的排列顺序由于animal_type给了默认值，无需通过实参来指定动物类型，因此在函数调用中只包含一个实参，然而python依然将这个
#实参当作位置实参，他依然会按位置顺序关联，所以要将pet_name放在形参列表开头
#现在调用函数后可以只输入一个实参

#如果要描述的动物不是小狗，可使用类似于下面的函数调用:
describe_pet(pet_name='harry',animal_type='hamster')
#由于显式的给animal_type提供了实参 ，因此python将忽略这个形参的默认值

#注意，使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出右默认值的实参。这让python已让能够正确的解读位置实参

#等效函数的调用
#可以混合使用位置实参，关键字形参和默认值，通常由多种等效的函数调用方式例如
'''def describe_pet(pet_name,animal_type='dog'):'''
#基于这种定义，再任何情况下，都必须给pet_name提供实参；指定该实参时可以使用位置方式，也可以使用关键字方式。
# 如果要描述的动物不是小狗，还必须再函数调用中给animal_type提供实参；同样指定改是处女的方式由位置方式和关键字方式

#一条名为whillie的小狗
describe_pet('whillie')
describe_pet(pet_name='whillie')

#一只名为Harry的仓鼠
describe_pet('harry',animal_type='hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')

#避免实参错误
#等你开时使用函数后可能会遇到实参不匹配错误。你提供的实参多余或少于函数完成其工作所需的信息时，将出现实参不匹配错误
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\n I have a " + animal_type + ".")
    print("My" + animal_type + "'s name is" + pet_name.title() + ".")

#describe_pet()
#File "D:/python/czpython/day62/function.py", line 98, in <module>  指出错误发生的地点
#TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
#指出了导致问题的函数调用，少调用的两个实参，并指出相应形参的名称
#给变量和函数名指定描述性名称，如果发生错误可以更容易找到

def make_shirt(size,sentence='I Love Python'):
    print("This shirt's size is " + size + " The label of the shirt is " + sentence)
make_shirt('L','SA GOU WEI WANG')
make_shirt(size='L',sentence='SA GOU WEI WANG')
make_shirt('L')

def make_city(courtry,nation='China'):
    print(courtry +" is in " + nation)
make_city('zhengzhou','China')
make_city('zhumadian')
make_city('Munich',nation = 'Germany')

#返回值

