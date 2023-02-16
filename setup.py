# -*- coding: utf-8 -*-

"""
@author: 赫凯
@software: PyCharm
@file: setup.py
@time: 2023/2/16 11:14
"""

import os
import setuptools

REQUIRED = [
    # 'tensorflow==2.9.1'
]

setuptools.setup(
    name='mydemo',
    version='1.0',
    description='A MySDK for python sdk_demo.',  # 一个简要的介绍而已
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        )
    ).read(),
    packages=setuptools.find_packages(),
    include_package_data=True,
    author='heKai',
    author_email='hekaiiii@163.com',
    # install_requires=REQUIRED,
)
