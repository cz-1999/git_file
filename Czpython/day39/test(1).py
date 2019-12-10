

import re

from Grainpy.extractor import Base
from Grainpy.draw import *


def combine_test():
    """
    测试base
    :return:
    """
    base1 = Base('127.0.0.2', 'root', '2333333', 'barn', 3306)
    base2 = Base('127.0.0.2', 'root', '2333333', 'barn3', 3306)

    barns1_times = base1.get_tables_name()
    new_table = base1.new_barn(barns1_times)
    base1.combine(barns1_times, new_table, base2)


def draw_test():
    """
    测试绘制时间序列温度散点图
    :return:
    """
    base2 = Base('127.0.0.2', 'root', '2333333', 'barn3', 3306)
    barn_name = '上河湾分库_1号罩棚'
    barn_name, time, temperature = base2.point_temperate(barn_name, 1, 1, 1)
    draw1(barn_name, time, temperature)


if __name__ == '__main__':
    #combine_test()
    draw_test()