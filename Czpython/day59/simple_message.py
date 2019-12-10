#变量
a = 'hello world'
print(a)
a = 'hello world2'
print(a)
#字符串 字符串就是一系列字符，在python中用 引号括起来的都是字符串，引号可以是单引号，也可以是双引号

#使用方法修改字符串的大小
name = 'ada lovelace'

print(name.title())#title()以首字母大写的方式显示每个单词，机每个单词的首字母都改为大写,函数title()不需要额外的信息，因此他后面的括号是空的

print(name.upper())#将所有字母转换为大写
print(name.lower())#将所有字母转换为小写

#合并连接字符串
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' +last_name
print(full_name)
#python中可以用+号来合并字符串。在这个示例中，我们用+来合并first_name,空格,last_name,以得到完整的姓名
print("Hello, "+full_name.title() + '!')
message = 'Hello, ' + full_name.title() +'!'
print(message)
#使用制表符或换行符来添加空白
#在编程中，空白泛指非打印字符，如空白符，制表符和换行符，要在字符串中添加制表符，可使用\t, 换行符\n
print('python')
print('\tpython')
print('Languages:\nPython\nC\nJavaScript')
print('Langeuages:\n\tPython\n\tC\n\tJavaScript')
#删除空白
#'python'和'python ',看起来几乎没什么两样，它们却是两个不同的字符串，python能够找出字符串开头和末尾多余的空白
#可使用方法strip(), lstrip()删除字符串最左端（开头）空白 ,rstrip()删除字符串最右端(结尾)空白，strip()删除字符串开头结尾空白

favorite_language = ' python '
print(favorite_language)
print(favorite_language.lstrip())
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.strip())
#对变量favorite_language调用方法rstrip()后这这多余的空格被删除了，然而这种删除是暂时的，再次输出favorite_language时，依然存在空白
#要用就删除这个字符串中的空白，必须将删除操作的结果存回到变量里

#使用字符串时避免语法错误
#语法错误是一种时不时会遇到的错误，程序中包含非法的python代码时，就会导致语法错误，例如在但单引号括起来的字符串中如果还包括单引号，就会引起错误
#python中' ， " ， ''' 都能用来括起来字符串，按照需求悬着相应的引号

meaasge = "One of Python's strengths is its diverse community."
print(meaasge)
#单引号位于两个双引号之间，因此python解释器能够正确的理解这个字符串，然而如果使用单引号,python将无法判断字符串的起始位置，会产生语法错误

#message = 'One of Python's strengths is its diverse community.'
#print(message)

#编写程序时，编辑器的语法突出功能可以榜知你快速找出某些语法错误，看到python代码以普通句子的颜色显示，或者普通句子依python代码的颜色显示时就可能一位着
#文件中存在引号不匹配的情况


