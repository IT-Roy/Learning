# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 9:33 PM
# @Author  : WangHuan
# @Email   : wanghuan_ch@163.com
# @File    : spider.py
# @Software: PyCharm

import requests
from lxml import html

def main():
    url = "https://music.douban.com"
    response = requests.Session().get(url)
    resHtml = html.fromstring(response.text)
    result = resHtml.xpath('//tr//a/text()')
    print(result)


if __name__ == "__main__":
    main()