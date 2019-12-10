'''
郑州附属中学（初中部）八年级"三率一分"分析软件
版本号： V1.0
编写人：肖乐
时间：2019年10月13日
摘要：
    本软件初步实现了该校八年级所有班和所有课程成绩的“优秀率、良好率、及格率和平均分”（简称“三率一分”）的自动统计分析。
解决了由于课程门数、班数、人数等变化大，仅使用Excel公式修改繁琐的问题。实现了任意课程门数、对任意班数和不同人数的自动
分析。
输入：符合一定格式的原始成绩Excel文件。
输出：各班以及全年级的“三率一分”excel文件。
未实现功能：
1，目前一些参数由全局变量提供，将来应该为命令行参数；
2，没有生成分析图片。
重构：
1.要提炼出函数;
2.尽量pythonic;
3.代码应更清晰易懂
'''

import pandas as pd
import numpy as np
import xlrd as xl
'''
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
'''
##############全局变量##############
COURSE_NUMBER = 8  # 课程门数
EXCELLENT = 80     # 优秀分数线
GOOD = 70          # 良好分数线
PASS = 60          # 及格分数线
##############全局变量##############


################  <初始化分析dataframe（df_anla）>################
df_dict= dict()
score_excel=xl.open_workbook('八年级成绩.xlsx')
for sheet in score_excel.sheets():
    df = pd.read_excel('D:\python\czpython\day57\八年级成绩.xlsx', sheet_name=sheet.name)
    df_dict[sheet.name] = df
col_list = [str(key) for key in df_dict]
col_list.insert(0, '统计内容')
col_list.append('全年级')
np_anla = np.array([col_list])
################  </初始化分析dataframe（df_anla）>##################


#################<计算所有课程的各班及全年级分析数据>#################
list_anla=list()
for i in range(4, 4+COURSE_NUMBER):
    t_list = [0, 0, 0, 100, 0, 0, 0, 0, 0, 0]
    course_name = np.array([df.columns.values[i]] * 9)
    anla_name = np.array(['平均分', '最高分', '最低分', '优秀人数', '优秀率', '良好人数', '良好率', '及格人数', '及格率'])
    course_anla = [*map(lambda m, n: m + n, course_name, anla_name)]
    list_anla.clear()
    list_anla = list_anla + course_anla
    for key in df_dict:
        ss = df_dict[key].iloc[:, i]
        list_anla.append(round(ss.mean()))
        max_tem=ss.max()
        list_anla.append(max_tem)
        min_tem=ss.min()
        list_anla.append(min_tem)
        li_temp = (sum(map(lambda k: k >= EXCELLENT, ss))),\
        (sum(map(lambda k: k >= GOOD, ss))),\
        (sum(map(lambda k: k >= PASS, ss)))
        l = len(df_dict[key])
        for j in li_temp:
            list_anla.append(j)
            list_anla.append(round(j*100/l,2))
        t_list =[t_list[0] + sum(ss), t_list[1] + l, (max_tem if t_list[2] <= max_tem else t_list[2]),\
                (min_tem if t_list[3] >= min_tem else t_list[3]),  t_list[4] + li_temp[0], 0,t_list[6] + li_temp[1],\
                 0,t_list[8] + li_temp[2],0]
    t_mean = round(t_list[0]/t_list[1],2)
    t_list[5] = round(t_list[4]*100/t_list[1],2)
    t_list[7] = round(t_list[6]*100/t_list[1],2)
    t_list[9] = round(t_list[8]*100/t_list[1],2)
    list_anla.append(t_mean)
    list_anla = list_anla + t_list[2:10]
    np_anla=np.vstack((np_anla,np.array(list_anla).reshape(len(col_list), 9).transpose()))
#################</计算所有课程的各班及全年级分析数据>#################


df_anla=pd.DataFrame(np_anla) # 转换成dataframe
df_anla.to_excel('D:\python\czpython\day57\分析表.xlsx') #写入excel




