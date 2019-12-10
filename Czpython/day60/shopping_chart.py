

product_list = [
    ('Iphone',5800),
    ('Mac pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Alex Python',120)
]
shopping_list = [] #购物车列表

salary = input('Input your salary:')#不能直接强转，因为不能判断输入的字符串是否是数字的形式
if salary.isdigit(): #如果输入的字符串是数字的形式
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list): #enumerate的作用是将列表中元素的下标和元素合成一个元组，
            # index会对应元组中的第一个元素，item会对应元组中的第二个元素
            #print(product_list.index(item),item)#用元素的下标作为产品编号
            print(index,item)
        user_choice = input('选择要买嘛?>>>')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice <len(product_list) and user_choice>=0:
                p_item = product_list[user_choice]
                if salary >= p_item[1]:  #买的起
                    salary-=p_item[1]
                    shopping_list.append(p_item)
                    print('Added %s into shopping chart,your current banlance is %s'%(p_item[0],salary))
                else:
                    print('你的余额还剩%s啦,还买个毛线'%(salary))
            else:
                print('Product code [%s] is not exist'%user_choice)
        elif user_choice == 'q':
            print('---------shopping_list----------')
            for p in shopping_list:
                print(p)
            print('Your current banlance is %s',salary)
            exit()
        else:
            print('invalid option')

