import os

filenames = os.listdir('C:/Users\cz1999\Desktop\data\data')


print(filenames)

#filenames=os.listdir(dir)    filenames.sort(key=lambda x:int(x[:-4]))
# #倒着数第四位'.'为分界线，按照‘.’左边的数字从小到大排序
# 此时乱序就变成了顺序：filenames=['11.jpg' , '22.jpg' , '30.jpg']，即filenames[1]='22.jpg';
# 当然可根据自己文件名的特征去决定int(x[:?])中？的值，从哪里去分割排序。
