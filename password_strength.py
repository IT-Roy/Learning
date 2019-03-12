# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 8:57 PM
# @Author  : WangHuan
# @Email   : wanghuan_ch@163.com
# @File    : password_strength.py
# @Software: PyCharm

def main():
    try_times = 5
    while try_times > 0:
        password = input("Please input your password: ")
        #length
        if len(password) < 8:
            try_times -= 1
            print("Sorry your password too short !")
        else:
            #only numbers
            for c in password:
                if c.isdecimal():
                    try_times -= 1
                    print("Your password strength very weak!")
                    break
            #only letters
            for c in password:
                if c.isalpha():
                    try_times -= 1
                    print("Your password strength very weak!")
                    break
    if try_times == 0:
        print("Too many try!")
if __name__ == "__main__":
    main()