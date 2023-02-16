# -*- coding: utf-8 -*-

"""
@author: 赫凯
@software: PyCharm
@file: shuchu1.py
@time: 2023/2/16 10:33
"""

import os
from glob import glob


def output__(dirname):
    if glob(dirname):
        for f in glob(dirname):
            if f[-4:] == '.txt':
                print(f)
                with open(f, encoding='utf-8') as f_:  # 打开文件
                    print(f_.read())  # 读取文件

            else:
                output__(f + '\*')


def shuchu1(file_name):
    # 获取上上级目录
    print(os.path.abspath(os.path.join(os.getcwd(), "../..")))
    output__(file_name)


if __name__ == '__main__':
    # 因为这个是在code1文件夹下，所以找data需要向前跳两级
    output__(os.path.abspath(os.path.join(os.getcwd(), "../..") + '/data/*'))
