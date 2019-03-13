# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 9:24 PM
# @Author  : WangHuan
# @Email   : wanghuan_ch@163.com
# @File    : dictionary.py
# @Software: PyCharm

import codecs

def dictionary(key):
    f = codecs.open("dict_utf.txt","r",encoding="utf-8")
    dict = {}
    for i in f.readlines():
        print(i)
        if i.find("\t\n") != -1:
            str = i.split("\t\n")
            dict[str[0]] = str[1]
    print(dict)
    #return result

def main():
    print("######################################")
    print()
    print("               超级词典                ")
    print()
    print("######################################")
    key = input("请输入单词（首字母大写）：")
    dictionary(key)

if __name__ == '__main__':
    main()