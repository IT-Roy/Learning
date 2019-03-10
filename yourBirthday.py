# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 10:47 PM
# @Author  : WangHuan
# @Email   : wanghuan_ch@163.com
# @File    : yourBirthday.py
# @Software: PyCharm

import datetime

def is_leap_year(year):
    leap_year = False
    if (year % 100 == 0) or (year % 4 == 0) and (year % 100 != 0):
        leap_year = True
    return leap_year

#判断输入日期是一年中的第几天
def date_processed(date):
    year = date.year
    month = date.month
    day = date.day
    days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = sum(days_in_month[: month - 1]) + day
    #判断闰年
    if month > 2 and is_leap_year(year):
        day += 1
    print("this is {} day".format(days))

#主函数
def main():
    birthday = input("Please input your birthday (yyyy/mm/dd): ")
    birthday_str = datetime.datetime.strptime(birthday,"%Y/%m/%d")
    date_processed(birthday_str)
    #print(birthday_str)

if __name__ == "__main__":
    main()