import requests
from bs4 import BeautifulSoup
import re

import time

def get_response(url):

    ip = '47.104.96.77'  # 这里用了一个代理ip

    headers = {
        'Referer': r'https://cn.bing.com/',
        'sec-ch-ua': '''"Microsoft Edge";v = "93", " Not;A Brand";v = "99", "Chromium";v = "93"''',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '''"Windows"''',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.44'
    }
    response = requests.get(url, headers=headers, timeout=30, params=ip)
    print(response)
    time.sleep(1)
    return response

def get_imags(response):
    global links
    bs = BeautifulSoup(response.text, 'html.parser')
    pics = bs.find_all('div', 'pic')
    for pic in pics:
        links.append(pic.find('img').attrs['src'])

import os

def download_imags(links):
    # 第一次使用时先创建一个文件夹
    os.mkdir('images')

    for i in range(len(links)):
        path = './images/{}.jpg'.format(i + 1)
        res = requests.get(links[i])
        with open(path, 'wb') as f:
            f.write(res.content)
        print('{}.jpg has been saved'.format(i + 1))


def get_data(response):
    global data_list
    bs = BeautifulSoup(response.text, 'html.parser')
    hds = bs.find_all('div', 'hd')
    bds = bs.find_all('div', 'bd')
    del bds[0]  # 第一项会读取一个空列表，要删除它
    stars = bs.find_all('div', 'star')
    items = bs.find_all('div', 'item')

    title_list = []  # 电影名
    for hd in hds:
        title = re.findall('[\u4E00-\u9fa5]+', str(hd.find('span', class_='title')))
        title_list.append(title)

    director_list = []  # 导演
    lead_list = []      # 主演
    type_list = []      # 类型
    date_list = []      # 年份
    for bd in bds:
        lst1 = re.findall('[\u4E00-\u9fa5]+', str(bd.find('p', class_='')))
        # print(lst1)
        # ['导演', '彼得', '杰克逊', '主演', '伊利亚', '伍德', '西恩', '新西兰', '美国', '剧情', '动作', '奇幻', '冒险']

        count = 0
        for elem in lst1:
            if (elem == '主演'):
                break
            count += 1
        director = lst1[1:count]
        director_list.append(director)

        if (count < len(lst1)):
            lead = lst1[count+1]  # 主演只取了第一项
            lead_list.append(lead)
        else:
            lead_list.append(" ")

        typ = lst1[-1]  # 类型只取了最后一项
        type_list.append(typ)

        date = re.findall('\d+', str(bd.find('p', class_='')))
        date_list.append(date)

    star_list = []  # 评分
    for star in stars:
        st= re.findall('[0-9]*\.?[0-9]', str(star.find('span', class_='rating_num')))
        star_list.append(st)

    quote_list = []  # 评语
    for quote in items:
        quo = re.findall('[\u4E00-\u9fa5]+', str(quote.find('span', class_='inq')))
        if len(quo) != 0:
            quote_list.append(quo)
        else:
            quote_list.append(" ")

    for i in range(len(quote_list)):
        data = []
        data.append(title_list[i])
        data.append(director_list[i])
        data.append(lead_list[i])
        data.append(date_list[i])
        data.append(type_list[i])
        data.append(star_list[i])
        data.append(quote_list[i])
        data_list.append(data)

import xlwt

def save_data(data_list, save_path):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheel = book.add_sheet('top250', cell_overwrite_ok=True)
    # 列标题
    col = ('电影名', '导演', '主演', '年份', '电影类型', '评分', '评语')
    # 添加列标题
    for i in range(len(col)):
        sheel.write(0, i, col[i])
    # 添加每一行记录
    for i in range(len(data_list)):
        data = data_list[i]
        for j in range(len(data)):
            sheel.write(i+1, j, data[j])
    book.save(save_path)

import collections
import pandas as pd
from matplotlib import pyplot as plt
import xlrd

# 画一个柱状图，按年份统计电影数量
def drawdata(save_path):
    # 读取数据
    df = pd.read_excel(save_path)
    show_time = list(df["年份"])
    show_time_count = collections.Counter(show_time)
    # 取数量最多的前10  得到一个列表
    # (年份, 数量)
    show_time_count = show_time_count.most_common(10)
    show_time_dic = {k: v for k, v in show_time_count}
    # 按年份排序
    show_time = sorted(show_time_dic)
    # 年份对应高分电影数量
    counts = [show_time_dic[k] for k in show_time]
    plt.figure(figsize=(9, 6), dpi=100)
    # 设置字体
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    # 绘制条形图
    plt.bar(show_time, counts, width=0.5, color="cyan")
    # y轴刻度重新设置一下
    plt.yticks(range(0, 16, 2))
    # 添加描述信息
    plt.xlabel("年份")
    plt.ylabel("高分电影数量")
    plt.title("上映高分电影数量最多的年份Top10", fontsize=15)
    # 添加网格  网格的透明度  线条样式
    plt.grid(alpha=0.2, linestyle=":")
    plt.show()

if __name__ == '__main__':
    links = []
    data_list = []
    for i in range(10):
        url = "https://movie.douban.com/top250?start={}&filter=".format(i * 25)
        response = get_response(url)
        get_imags(response)
        get_data(response)
    download_imags(links)
    save_path = './top250.xls'
    save_data(data_list, save_path)
    drawdata('top250.xls')
