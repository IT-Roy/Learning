# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 12:17 AM
# @Author  : WangHuan
# @Email   : wanghuan_ch@163.com
# @File    : server.py
# @Software: PyCharm

import socket

def main():
    PORT = 8888
    s = socket.socket()
    HOST = socket.gethostname()
    s.bind((HOST, PORT))
    s.listen(5)

    while True:
        a, ads = s.accept()
        print(ads)
        msg = '你好啊'
        a.send(msg.encode('utf-8'))
        a.close()

if __name__ == "__main__":
    main()