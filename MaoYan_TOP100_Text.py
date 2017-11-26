#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/11/26 0:02 
# @File : MaoYan_TOP100_Text.py 
# @Software: PyCharm

import requests
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Referer': 'http://maoyan.com/board/4?offset=0'}


# 获取请求页面
def getPage(url):
    try:
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception:
        return None


# 获取电影信息
def getInfo(html):
    # 正则匹配出电影的索引、海报、电影名、主演、评分
    pattern = re.compile(
        '<dd>.*?<i class="board-index.*?>(\d+)</i>.*?<img data-src="(.*?)".*?<p class="name">'
        '<a.*?>(.*?)</a>.*?<p class="star">(.*?)</p>.*?'
        '<p class="releasetime">(.*?)</p>.*?<i class="integer">(.*?)</i><i class="fraction">(.*?)</i>.*?</dd>',
        re.S)

    items_list = re.findall(pattern, html)
    for item in items_list:
        yield {
            'index': item[0],  # 索引
            'image': item[1],  # 海报
            'name': item[2],  # 电影名
            'actor': item[3].strip()[3:],  # 主演
            'time': item[4].strip()[5:],  # 上映时间
            'score': item[5] + item[6]  # 评分
        }


# 采用这种方法写入数据耦合性高
# def writeData(content):
#     fout = open('Movies_Info.txt', mode='a', encoding='utf-8')
#     for item in content:
#         fout.write(json.dumps(item, ensure_ascii=False) + '\n')
#         fout.write('---------------------------\n')
#     fout.close()

def writeData(field):
    with open('Movies_Info_Text.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(field, ensure_ascii=False) + '\n')  # json.dumps 用于将 Python 对象编码成 JSON 字符串，若对象为字符串是无法写入文本的
        f.close()


if __name__ == '__main__':
    # html_list = []
    # for num in [i*10 for i in range(11)]:
    #     url = 'http://maoyan.com/board/4?offset=' + str(num)
    #     html = getPage(url)
    #     html_list.append(html)
    for num in [i * 10 for i in range(11)]:
        url = 'http://maoyan.com/board/4?offset=' + str(num)
        html = getPage(url)
        for item in getInfo(html):
            print(item)
            writeData(item)
