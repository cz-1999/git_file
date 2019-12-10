import pandas as pd
import re


creat = """CREATE TABLE {} (
  `barn_id` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `barn_name` varchar(254) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `time` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `row` int(225) NOT NULL,
  `layer` int(225) NOT NULL,
  `column` int(225) DEFAULT NULL,
  `temperature` double(225,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
"""

def prise():
    data = pd.read_csv('C:/Users\cz1999\Desktop/3.txt', sep=';', header=None, encoding='gbk')
    s = []
    for i in range(0, 11322):
        s.append(data[0][i])
    s1 = []
    for i in s:
        s1.append(re.search('INSERT\sINTO\s(.*?)\sVALUES', i).group(1))
    print(set(s1))
    for barn in set(s1):
        print(creat.format(barn), '\n')
#__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。
# 这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
if __name__ == '__main__':
    prise()

"""
c = {'s':s1}
data1 = DataFrame(c)
print(data1.drop_duplicates())

data2 = data1.drop_duplicates()
print(data2['s'])
print(len(list(data2['s'])))


#s2=[]
#for i in range(0,68):
    #s2.append(data2['s'][i])
s2 = list(data2['s'])
print(list(data2['s']))
for i in s2:
    print(i)
"""








