#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   quickSort.py
@Time    :   2021/08/25 11:20:44
@Author  :   WH
@Version :   1.0
@Contact :   1049346505@qq.com
@License :   (C)Copyright 2021-2022, WangHuan
@Desc    :   None
'''

# here put the import lib
import random
from cal_time import *
import sys

def partation(list,left,right):
    tmp = list[left]
    while left < right:
        while left < right and list[right] >= tmp:
            right -= 1
        list[left] = list[right]
        while left < right and list[left] <= tmp:
            left += 1
        list[right] = list[left]
    list[left] = tmp
    return left

def quickSort(list,left,right):
    if left < right:
        mid = partation(list,left,right)
        quickSort(list,left,mid-1)
        quickSort(list,mid+1,right)
        

def main():
    test = list(range(20))
    random.shuffle(test)
    print(test)
    #insertSort(test)
    quickSort(test, 0, len(test)-1)
    #partation(test, 0, len(test)-1)
    print(test)

if __name__ == "__main__":
    main()