# 传递列表
# 你会发现，像函数中传递列表很有用，这种列表中可能包含的是名字，数字，或者更复杂的对象（如字典）
# 将列表传递给函数后，函数就能直接访问其内容，使用函数来提高使用列表的效率

# 假设由一个永华列表，要问候其中的每一位用户
def greet_users(names):
    """向列表中每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['weiwang', 'zhenwei', 'lihao']
greet_users(usernames)

# 在函数中修改列表
# 将函数传进列表后，函数就可对其进行修改，在函数中，对列表所做的任何修改都是永久性的

# 来看一家为用户提交的设计制作3D打印模型的公司。需要打印的设计存储在一个列表中，打印后的一道另一个列表中
# 下面是不适应函数的情况下模拟这个过程的代码:

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表complied_models中
while unprinted_designs:  #只要列表中还有数据，就进行循环
    current_design = unprinted_designs.pop()  # 从列表末尾删除一个设计，将其存储到变量current_design中
    # 模拟根据设计制作3D打印模型的全过程
    print('Printing model: ' + current_design)
    completed_models.append(current_design)
# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# 这个程序首先要创建一个需要打印的设计列表，还创建一个名为completed_models的空列表，每个设计打印都将移到这个列表中。
#只要列表unprinted_designs中还有设计，while循环就模拟打印设计的过程: 从该列表末尾删除一个设计，将其存储到变量current_design中，
#并显示一条消息，指出正在打印当前的设计，在将该设计加入列表completed_model中。循环结束后显示已打印的所有设计


#重新组织代码，编写两个函数，每个都做一件具体的工作，大部分代码都与原来的相同，只是效率更高，第一个函数负责打印设计工作，第二个函数负责概述打印
#了那些设计

def print_models(unprinted_designs,completed_models):
    # 模拟打印每个设计，直到没有未打印的设计为止
    # 打印每个设计后，都将其移到列表complied_models中
    while unprinted_designs:  # 只要列表中还有数据，就进行循环
        current_design = unprinted_designs.pop()  # 从列表末尾删除一个设计，将其存储到变量current_design中
        # 模拟根据设计制作3D打印模型的全过程
        print('Printing model: ' + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    # 显示打印好的所有模型
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#函数printed_models(),包含两个形参:一个需要打印的列表模型和一个打印好的列表模型。给定这两个列表，给定这两个列表，函数模拟打印每个设计的过程:
#将设计逐个的从未打印的列表中取出，并加入打印好的列表中

#函数show_completed_models()包含一个形参:打印好的模型列表，给定这个列表，函数显示打印出来的每个模型的名称
#这样会使组成序更加简洁，已于理解和维护


#这个程序演示了这样一种理念，即每个函数都应只负责一项具体的工作。第一个函数打印每个设计，而第二个函数显示打印好的模型。
# 这优于使用一个函数来完成两项工作。编写函数是如果你发现他执行的任务太多,请尝试将这些代码分到两个函数中，
# 别忘了总是可以在一个函数中调用另一个函数，这有助于将复杂的任务划分称一系列的步骤。


#禁止函数修改列表
#有时候需要禁止函数修改列表，例如，像前一个示例一样，你有一个未打印的设计列表并编写了一个将这些设计移到打印好的列表中的函数，即便打印完所有的
#设计后，也要保留原来的未打印的设计列表，以供备案。但是所有设计都移了出去，原来的列表变成了空的，为了解决这个问题可以像函数传递副本，而不是原件
#这样函数所作的任何修改斗志影星副本而不影响原件，

#function_name(list_name[:])
#切片表示法[:]创建列表的副本。如果不想被改变列表里的设计可以这样调用列表
#print_models(unprinted_designs[:],completed_models)

#这样函数依然能完成工作修改的是副本，虽然向列表中传递副本可保留列表的内容，但除非有充分理由需要传递副本，否则应该将原始列表传给函数，因为让函数
#使用现成列表可避免花时间和内存创建副本，从而提高效率，在处理大型列表时尤其如此


