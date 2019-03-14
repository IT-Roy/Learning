# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 9:43 PM
# @Author  : WangHuan
# @Email   : wanghuan_ch@163.com
# @File    : GBK_to_UTF-8.py
# @Software: PyCharm

import codecs

class codeConversion:
    """
    编码转换类
    """
    def __init__(self, src ,dst):
        self.src = src
        self.dst = dst

    def GBK_TO_UTF8(self):
        f_in = codecs.open(self.src, 'r', 'gb18030')
        f_out = codecs.open(self.dst, 'w', 'utf-8')
        f_out.write(f_in.read())

    def UTF8_TO_GBK(self):
        f_in = codecs.open(self.src, 'r', 'utf-8')
        f_out = codecs.open(self.dst, 'w', 'gb18030')
        f_out.write(f_in.read())

# #文件读取
# def read_file(filePath,encoding=""):
#     f = codecs.open(filePath, 'r', encoding)
#     return f.read()
#
# #文件写入
# def write_file(filePath, file, encoding=""):
#     f = codecs.open(filePath, 'w', encoding)
#     f.write(file)
#
# #gbk2utf-8
# def GBK_2_UTF8(src, dst):
#     content = read_file(src, encoding="gb18030")
#     write_file(dst, content, encoding="utf-8")
#
# #utf2gbk
# def UTF8_2_GBK(src, dst):
#     content = read_file(src, encoding="utf-8")
#     write_file(dst, content, encoding="gb18030")

def main():
    #GBK_2_UTF8("dict_gbk.txt", "dict_utf.txt")
    #编码转换类的实例
    code_conversion = codeConversion("dict_gbk.txt", "dict_utf2.txt")
    code_conversion.GBK_TO_UTF8()

if __name__ == "__main__":
    main()