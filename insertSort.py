#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   insertSort.py
@Time    :   2021/08/24 11:01:59
@Author  :   WH
@Version :   1.0
@Contact :   1049346505@qq.com
@License :   (C)Copyright 2021-2022, WangHuan
@Desc    :   None
'''

# here put the import lib
import random

def insertSort(list):
    
    for i in range(1,len(list)):
        j = i -1 
        temp = list[i]
        while j >= 0 and  temp > list[j]:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = temp
        print(list)



def main():
    test = list(range(20))
    random.shuffle(test)
    print(test)
    insertSort(test)

if __name__ == "__main__":
    main()