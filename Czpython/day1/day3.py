name = input("name:")#字符串不能强转为int型
print(type(name))#打印出变量类型
age = input("age:")
print(type(age),type(int(age)))
print(name,age)
info = '''
--------- info of {0} --------
name: {0}
age: {1}
'''.format(name,age)
print(info)


