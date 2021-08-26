#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   o(n**2)SortTime.py
@Time    :   2021/08/24 11:19:32
@Author  :   WH
@Version :   1.0
@Contact :   1049346505@qq.com
@License :   (C)Copyright 2021-2022, WangHuan
@Desc    :   None
'''

# here put the import lib
import random
from cal_time import *
import copy

@cal_time
def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j],list[i]
@cal_time
def selectSort(list):
    for i in range(len(list)-1):
        min_index = i
        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[min_index],list[i] = list[i],list[min_index]

@cal_time
def insertSort(list):
    
    for i in range(1,len(list)):
        j = i -1 
        temp = list[i]
        while j >= 0 and  temp > list[j]:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = temp

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
@cal_time
def do_quickSort(list):
    quickSort(list,0,len(list)-1)

def main():
    #test = random.sample(range(0,10000),10000)
    test = list(range(1000000))
    random.shuffle(test)
    test1 = copy.deepcopy(test)
    test2 = copy.deepcopy(test)
    test3 = copy.deepcopy(test)
    test4 = copy.deepcopy(test)
    #bubbleSort(test1)
    #selectSort(test2)
    #insertSort(test3)
    do_quickSort(test4)

if __name__ == "__main__":
    main()