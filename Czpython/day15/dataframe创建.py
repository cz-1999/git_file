import numpy as np
import pandas as pd
from pandas import DataFrame,Series

#dataframe是一种表格型的数据结构
#由按一定顺序排列的多列数据组成，设计初衷是将series的使用场景从一维扩展到多维
#dataframe既有行索引，又有列索引，行索引index,列索引columns,值values

#dataframe的创建
#使用ndarry创建dataframe
DataFrame(data=np.random.randint(60,100,size=(2,3)),index=['期中','期末'],columns=['张三','李四','王五'])
#不能用print表示出来
#使用字典创建dataframe


