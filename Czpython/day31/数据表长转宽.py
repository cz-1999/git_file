import pandas as pd
import numpy as np


mydata=pd.DataFrame({
"Name":["苹果","谷歌","脸书","亚马逊","腾讯"],
"Company":["Apple","Google","Facebook","Amozon","Tencent"],
"Sale2013":[5000,3500,2300,2100,3100],
"Sale2014":[5050,3800,2900,2500,3300],
"Sale2015":[5050,3800,2900,2500,3300],
"Sale2016":[5050,3800,2900,2500,3300]
       })



mydata1=mydata.melt(
id_vars=["Name","Company"],   #要保留的主字段
var_name="Year",                     #拉长的分类变量
value_name="Sale"                  #拉长的度量值名称
        )

print(mydata)
print(mydata1)