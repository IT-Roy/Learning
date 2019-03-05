# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 9:54 PM
# @Author  : WangHuan
# @Email   : wanghuan_ch@163.com
# @File    : turtle_draw_start.py
# @Software: PyCharm

import turtle

#绘图函数
def draw_starts(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    #递归调用
    if size < 100:
        size += 10
        draw_starts(size)


def main():
    turtle.pencolor("red")
    #turtle.pensize(10)
    draw_starts(50)
    turtle.exitonclick()

if __name__ == '__main__':
    main()