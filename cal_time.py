#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   cal_time.py
@Time    :   2021/08/24 11:30:39
@Author  :   WH
@Version :   1.0
@Contact :   1049346505@qq.com
@License :   (C)Copyright 2021-2022, WangHuan
@Desc    :   None
'''

# here put the import lib
import time
def cal_time(func):
    def wrapper(*args,**kwargs):
        t1=time.perf_counter()
        result=func(*args,**kwargs)
        t2=time.perf_counter()
        print("%s running time: %s sec." %(func.__name__,t2-t1))
        return result
    return wrapper