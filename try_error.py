# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 9:30 PM
# @Author  : WangHuan
# @Email   : wanghuan_ch@163.com
# @File    : try_error.py
# @Software: PyCharm

def main():
    quit_or_goon = input("是否退出程序 Y/N：")
    while quit_or_goon != "Y":
        usrInput = input("请输入您的性别、年龄、身高（cm） （以空格分隔）：")
        try:
            arr = usrInput.split(" ")
            sex = arr[0]
            age = int(arr[1])
            height = int(arr[2])
            print("******************************")
            print("您的性别是{},年龄是{},身高是{}cm".format(sex, age, height))
            print("******************************")
            quit_or_goon = input("是否退出程序 Y/N：")
        except:
            print("输入信息有误")

if __name__ == "__main__":
    main()