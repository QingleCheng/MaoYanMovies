#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/11/26 0:09 
# @File : MaoYan_TOP100_MulProcess.py 
# @Software: PyCharm

# 多进程爬取数据
# 但是因为多进程的原因，返回数据顺序会不一致


import requests
import re
import json
from multiprocessing import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}


def getPage(url):
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        return response.text
    else:
        return None


def getInfo(html):
    pattern = re.compile(
        '<dd>.*?<i class="board-index.*?>(\d+)</i>.*?<img data-src="(.*?)".*?<p class="name">'
        '<a.*?>(.*?)</a>.*?<p class="star">(.*?)</p>.*?'
        '<p class="releasetime">(.*?)</p>.*?<i class="integer">(.*?)</i><i class="fraction">(.*?)</i>.*?</dd>',
        re.S)
    items_list = re.findall(pattern, html)
    for item in items_list:
        yield {
            'index': item[0],
            'image': item[1],
            'name': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def writeData(field):
    with open('Movies_Info_MP.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(field, ensure_ascii=False) + '\n')
        f.close()


def main(num):
    url = 'http://maoyan.com/board/4?offset=' + str(num)
    html = getPage(url)
    for item in getInfo(html):
        print(item)
        writeData(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i * 10 for i in range(10)])  # 与内置的map函数用法行为基本一致，它会使进程阻塞直到返回结果。
    pool.close()  # 关闭进程池（pool），使其不在接受新的任务
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
