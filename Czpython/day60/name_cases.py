name = 'Eric'
message = 'Hello' + name + ',would you like to learn some Python today?'
print(message)
print(name.upper())
print(name.lower())
print(name.title())
famous_quotes = 'Albert Einstein once said,"A person who never made a mistake never tried anything new"'
print(famous_quotes)
name = '\tweiwang\n'
print(name.strip())
print(name.lstrip())
print(name.rstrip())

#数字

#整数，
# 在python中，可对整数执行加(+)减(-)乘(*)除(/)运算,python直接返回运算结果，python中两个*号表示乘方运算
print(2+3)
print(3-2)
print(2*3)
print(3/2)
print(2**3)
print(10**6)
# python还支持运算次序，因此在同一个表达式中使用多种运算可以使用括号来修改运算次序
print(2+3*4)
print((2 + 3 ) * 4)
#在示例中，空格不影响python计算表达式、

#浮点数
#python将带小数点的数字都称为浮点数
#从很大程度上来说，使用浮点数时无需考虑其行为，你只需要输入要使用的数字，Python通常都会按你期望的方式处理它们
print(0.1+0.1)
print(0.2+0.2)
print(2*0.1)
print(2*0.2)
#但需要注意的是结果包含的小数位可能是不确定的
print(0.2+0.1)
print(3*0.1)
#所有语言都存在这种问题，python换回尽力找一种方式以尽可能精确的表示结果，这在有些情况下很难，就现在而言暂时忽略多余的小数位即可，之后学习处理多余
#小数位的方式

#使用函数str()避免类型错误
#经常需要在消息种显示变量的值，若要祝人生日快乐
age =23
#message = 'Happy' +age +'rd Birthday'
#print(message)

#会发生类型错误，python无法识别你使用的信息，在这个例字种python知道你使用了一个值为整数(int)的变量，但它不知道该如何解读这个值，python知道这个
#变量表示的可能是数值23，也可能是字符2和3，像上面这样在字符串中使用整数时需要显式的指出你希望python将这个字符用作字符串，可调用函数str(),它让python
#非字符串值转化为字符串
message = 'Happy ' +str(age) +'rd Birthday'
print(message)

#注释 在python中注释用井号(#)标识。#号后面的内容会被python解释器忽略

import this


