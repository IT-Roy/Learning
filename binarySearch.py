#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   binarySearch.py
@Time    :   2021/07/21 22:11:00
@Author  :   WH
@Version :   1.0
@Contact :   1049346505@qq.com
@License :   (C)Copyright 2021-2022, WangHuan
@Desc    :   None
'''

# here put the import lib
def binarySearch(arr,tag):
    lens = len(arr)
    left = 0
    right = lens - 1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == tag:
            return mid
        if arr[mid] < tag:
            left = mid + 1
        else:
            right = mid - 1

def main():
    test = [2,4,8,11,34,35,44,46,55]
    tag = 11
    print(binarySearch(test,tag))

if __name__ == "__main__":
    main()
