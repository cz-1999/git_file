
#导入整个模块
import pizza1 #模块在主目录里，可以直接导入 import module_name  模块在分目录里，不可以直接导入 from list_name(目录名) import module_name

pizza1.make_pizzaplus1(16, 'pepperoni')
pizza1.make_pizzaplus1(12, 'mushrooms', 'green peppers', 'extra cheese')

#python读取这个文件是，代码行from day65 import pizza让python打开文件pizza.py,并将其中所有的函数都复制到这个程序中，你看不到复制的代码
#因为在这个程序运行时python在幕后赋值这些代码，你只需知道，在making_pizzas.py中，可以使用pizza.py中定义的所有函数


#从模块中导入特定函数                     模块在分目录里无法导入
#from module_name import function_name
#通过用逗号分隔函数名，可根据需要在函数中导入任意数量的函数、
#from module_name import function_0,function_1,function_2

from pizza1 import make_pizzaplus1
pizza1.make_pizzaplus1(16, 'pepperoni')
pizza1.make_pizzaplus1(12, 'mushrooms', 'green peppers', 'extra cheese')

#使用as 给模块取别名
#import module_name as mn
import pizza1 as pl

#使用as给函数取别名
#from module_name import function_name as fn
from pizza1 import make_pizzaplus1 as ml

#导入模块中的所有函数
from pizza1 import *
#import 语句中的星号，让python将模块pizza中的每个函数都复制到这个程序文件中。由于导入了每个函数，可通过名称来调用每个函数
#而无需使用句点表示法，最好不要使用这种方法 : python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数，
# 最佳的做法是要么导入需要使用的函数，要么导入整个模块并使用据点表示法，这能让代码更清晰更容易理解


#函数编写指南
"""
    编写函数时需要牢记几个细节，应给函数指定描述性名称。且只在其中使用小写字母和下划线，描述性名称可帮助你和别人明白代码想要做什么，给模块命
名时也应遵守上述规则
    每个函数都应该包含简要的阐述其功能的注释，盖住是应紧跟在函数定义后面，并采用文档字符串格式
    

给形参指定默认值时，等号两边不要有空格:
def function_name(parameter_0,parameter_1='default value')
对于函数调用中的关键字实参，也应遵循这种规定:
function_name(value_0,parameter_1='value')


建议代码行的长度不要超过79字符，这样只要编辑器窗口适中，就能看到整行代码，如果形参很多导致函数定义的长度超过了79字符
可在函数定义中输入左括号后按回车键，并在下一行按两次Tab键，从而将形参列表和值缩进一层的函数体分开来
    大多数都会自动对齐后续参数列表行，事情缩进程度与你给第一个参数列表行指定的缩进程度相同:
def function_name(
        parameter_0,parameter_1,parameter_2,
        parameter_3,parameter_4,parameter_5):
    function body...

如果程序或模块包含多个函数u，可使用两个空行将相邻的函数分开，这样将更容易知道前一个函数在什么地方结束，下一个函数从什么地方开始
    所有import 语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序










"""
