#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   bubbleSort.py
@Time    :   2021/08/24 10:55:31
@Author  :   WH
@Version :   1.0
@Contact :   1049346505@qq.com
@License :   (C)Copyright 2021-2022, WangHuan
@Desc    :   None
'''

# here put the import lib
import random


def bubbleSort(lists):
    for i in range(len(lists)):
        for j in range(len(lists)):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
        print(lists)



def main():
    test = random.sample(range(0, 100), 15)
    print(test)
    bubbleSort(test)


if __name__ == "__main__":
    main()