# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 12:26 AM
# @Author  : WangHuan
# @Email   : wanghuan_ch@163.com
# @File    : client.py
# @Software: PyCharm

import socket

def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 8888
    s.connect((host, port))
    msg = s.recv(1024)
    print(msg.decode('utf-8'))
    s.close()

if __name__ == "__main__":
    main()