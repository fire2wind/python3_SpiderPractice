#根据python3网络爬虫开发实战改的
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import time
import csv
def get_one_page(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in paser_one_page(html):
        info.writerows([item]) #不加[]会造成一个单元格只有一个字符

def paser_one_page(html):
    soup = BeautifulSoup(html,'lxml')
    node=soup.find(name='dd')
    #笨办法找节点，没想到用BeautifulSoup解析的好方法
    for i in range(10):
        node_name = node.find(name='p')
        name = node_name.string
        #print(name)
        node_star = node_name.find_next_sibling()
        star = node_star.string.strip()
        #print(star)
        node_time = node_star.find_next_sibling()
        time = node_time.string
        #print(time)
        node_score = node_time.find_next('p')
        score = float(node_score.i.string+node_score.i.find_next_sibling().string)
        #print(score)
        node = node.find_next_sibling()
        yield [name,star,time,str(score)]

if __name__ == '__main__':
    with open('maoyan.csv','w',encoding='utf-8',newline='') as fp:
        info = csv.writer(fp)
        info.writerow(['电影名','主演','时间','评分'])
        for i in range(10):
            main(offset=i*10)
            time.sleep(1)

        


