#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/11/26 0:10 
# @File : MaoYan_TOP100_Markdown.py 
# @Software: PyCharm

import requests
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Referer': 'http://maoyan.com/board/4?offset=0'}


def getPage(url):
    try:
        response = requests.get(url, headers=headers)
        # print(response.status_code)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception:
        return None


def getInfo(html):
    # 正则匹配出电影的索引、海报、电影名、主演、评分
    pattern = re.compile(
        '<dd>.*?<i class="board-index.*?>(\d+)</i>.*?<a href="(.*?)".*?<img data-src="(.*?)".*?<p class="name">'
        '<a.*?>(.*?)</a>.*?<p class="star">(.*?)</p>.*?'
        '<p class="releasetime">(.*?)</p>.*?<i class="integer">(.*?)</i><i class="fraction">(.*?)</i>.*?</dd>',
        re.S)

    items_list = re.findall(pattern, html)
    for item in items_list:
        yield {
            'index': item[0],
            'link': 'http://maoyan.com' + item[1],
            'image': item[2],
            'name': item[3],
            'actor': item[4].strip()[3:],
            'time': item[5].strip()[5:],
            'score': item[6] + item[7]
        }


def writeMarkdown(field):
    with open('Movies_Info_MD.md', mode='a', encoding='utf-8') as f:
        info_dict = json.dumps(field, ensure_ascii=False)
        print('----->' + info_dict)
        f.write('## No:' + field['index'] + '\n')  # 写入排名
        f.write('![image](' + field['image'] + ')\n')  # 写入海报，注意Markdown中插入图片的语法
        f.write('### **' + field['name'] + '** \n')  # 写入影片名
        f.write('#### **主演：**' + field['actor'] + '\n')  # 写入主演
        f.write('#### **上映时间：**' + field['time'] + '\n')  # 写入上映时间
        f.write('#### **评分：**' + field['score'] + '\n')  # 写入评分
        f.write('[了解更多...](' + field['link'] + ')\n\n')
        f.write('------\n')  # 写入分割线，在Markdown语法中至少三个'-'以上才能构成分割线
        f.close()


if __name__ == '__main__':
    for num in [i * 10 for i in range(11)]:
        url = 'http://maoyan.com/board/4?offset=' + str(num)
        html = getPage(url)
        for item in getInfo(html):
            # print(item)
            writeMarkdown(item)
