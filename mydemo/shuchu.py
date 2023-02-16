# -*- coding: utf-8 -*-

"""
@author: 赫凯
@software: PyCharm
@file: shuchu.py
@time: 2023/2/16 10:33
"""

import os
import mydemo.code1.shuchu1 as sc


def shuchu():
    # 因为这个是在code文件夹下，所以找data只需要向前跳一级
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))).replace('\\', '/')
    sc.shuchu1(path + '\data\*')


if __name__ == '__main__':
    print(os.path.abspath(os.path.join(os.getcwd(), "..")))
    shuchu()
