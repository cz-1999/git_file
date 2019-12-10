import pandas as pd
import re

creat = '''INSERT INTO `上河湾分库_2号库` SELECT * FROM {};'''
def prise():
    data = pd.read_csv('C:/Users\cz1999\Desktop/4.txt',sep=';',header=None,encoding='gbk')
    s=[]
    for i in range(0,2754):
        s.append(data[0][i])
    s1=[]
    for i in s:
        s1.append(re.search('INSERT\sINTO\s(.*?)\sVALUES',i).group(1))
    for i in set(s1):
        print(creat.format(i))
if __name__ == '__main__':
    prise()