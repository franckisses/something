from bs4 import BeautifulSoup
import urllib
from urllib import request
import re,time
import basicSpider
from UserAgentPool import *
from multiprocessing import Pool
from multiprocessing import Manager

def get_html(url):
    headers = {
        "User-Agent": UserAgent().user_agent()
    }
    req = request.Request(url,headers = headers)
    #进行错误回收
    try:
        response = request.urlopen(req)
        html = response.read().decode("utf-8")
    except urllib.URLError as e:
        html = None
        if hasattr(e,code) and  500 <= e.code < 600:
            html = get_html(url,user_agent,num_retries = -1)
    return html

def get_movie_all(html):
    soup = BeautifulSoup(html,"lxml")
    movie_list = soup.find_all("div",class_="bd doulist-subject")
    return  movie_list

def get_movie_one(movie):
    result = []
    soup_all = BeautifulSoup(str(movie),"lxml")

    title = soup_all.find_all("div",class_='title')
    soup_title = BeautifulSoup(str(title[0]),"lxml")

    for line in soup_title.stripped_strings:
        result.append(line)

    num = soup_all.find_all("span")
    result.append(num[1].contents[0])

    soup_num = BeautifulSoup(str(num[0]),"lxml")

    for line in soup_num.stripped_strings:
        result = result + line

    info = soup_all.find_all("div",class_ = "abstract")
    soup_info = BeautifulSoup(str(info[0]),"lxml")
    result_str = ""
    for line in soup_info.stripped_strings:
        result_str = result_str + "||" + line
    result.append(result_str)
    return result

def save_file(text,filename):
    with open(filename,"ab") as f:
        f.write(text.encode())


def crawlInfo(url,q):
    html = get_html(url)

    movie_list = get_movie_all(html)

    get_movie_one(movie_list[0])

    for movie in movie_list:
        result = get_movie_one(movie)
        text = '\t' + '电影名：' + str(result[0]) + ' | 评分：' + str(result[1]) + ' | ' + str(result[2]) + '\n'

    save_file(text,"doubanmovie.txt")

    minSecond = 1
    maxSecond = 5
    time.sleep(random.randint(minSecond, maxSecond))
    # 完成了当前url的抓取之后，put到队列中去


    q.put(url)


if __name__ == "__main__":
    # 创建进程池和队列来完成抓取
    pool = Pool()
    q = Manager().Queue()
    # 处理入口url信息
    send_url = "https://www.douban.com/doulist/46296008/?start=0&sort=seq&sub_type="
    crawlInfo(send_url,q)
    html = get_html(send_url)
    # 用正则去匹配翻页的页面信息
    pattern = re.compile("https://www.douban.com/doulist/46296008/\?start=.*?")
    itemurls = re.findall(pattern,html)

    #用队列与模拟广度优先遍历
    crawled_queue = []
    crawl_queue = []
    for itemurl in itemurls:
        # 第一步去重,通过已爬队列来放置重复
        if itemurl not in crawled_queue:
            crawl_queue.append(itemurl)
    #第二步去重,保证待爬队列本身不重复
    crawl_queue = list(set(crawl_queue))

    # 抓取队列的信息为空的时候,则退出循环,说明信息抓取完毕
    while crawl_queue:
        url = crawl_queue.pop()
        # crawlInfo(url)
        # 将已经爬过的url加入到已爬队列中
        pool.apply_async(func = crawlInfo, args=(url,q))
        # 当前的url抓取完成,添加到完成队列中
        url = q.get()
        crawled_queue.append(url)
    pool.close()
    pool.join()




