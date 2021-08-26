#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   selectSort.py
@Time    :   2021/08/24 09:44:34
@Author  :   WH
@Version :   1.0
@Contact :   1049346505@qq.com
@License :   (C)Copyright 2021-2022, WangHuan
@Desc    :   None
'''

# here put the import lib
import random

def selectSort(list):
    for i in range(len(list)-1):
        min_index = i
        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[min_index],list[i] = list[i],list[min_index]
        print(list)

def main():
    test = random.sample(range(1,100),20)
    print(test)
    print(len(test))
    print("***********************")
    selectSort(test)

if __name__ == "__main__":
    main()