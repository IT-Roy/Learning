# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 9:56 PM
# @Author  : WangHuan
# @Email   : wanghuan_ch@163.com
# @File    : turtle_draw_tree.py
# @Software: PyCharm

import turtle

#绘制函数
def draw_tree(length):
    #右半部分
    turtle.forward(length)
    turtle.right(20)
    turtle.forward(length - 15)
    #左半部分
    turtle.backward(length - 15)
    turtle.left(40)
    turtle.forward(length - 15)
    if length > 20:
        length -= 15
        draw_tree(length)

#主函数
def main():
    turtle.sety(-80)
    turtle.left(90)
    turtle.color("red")
    draw_tree(80)
    turtle.exitonclick()

if __name__ == '__main__':
    main()