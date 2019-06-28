# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      zhihu
   Description :    知乎来抓取网页上的文档 还存在缺陷
   Author :         gongyan
   Date：           2019/2/27
   Change Activity: 2019/2/27 20:17
-------------------------------------------------
"""

import requests
from pyquery import PyQuery as pq
from fake_useragent import UserAgent

url = 'http://www.zhihu.com/explore'
headers = {
    'User-Agent': UserAgent().chrome,
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': '_xsrf=TdyeKF3g59NaAQLurJpL5Uc1izZyTpKG; _zap=a5841a17-5a7a-43c4-9878-33734a33be59; d_c0="AOChTqMtrw6PTqCJgNK3JOaWxb8nYTKC1AE=|1545054183"; \
    z_c0="2|1:0|10:1545054230|4:z_c0|92:Mi4xdzloVkFBQUFBQUFBZ0NFN295MnZEaVlBQUFCZ0FsVk5GdllFWFFEMnhGX0JTaHctWlluSUg3eDlua2EzOUVUQ2JR|b3f1150f1205a63d30cefc3aa669fefe87726a84e18a8451edab7d2aaec4b509"; __utmz=51854390.1547196330.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/inbox/7912224000; __utmv=51854390.100-1|2=registration_date=20140501=1^3=entry_date=20140501=1; tst=r; tgw_l7_route=66cb16bc7f45da64562a077714739c11; q_c1=80c3216a63c54d78b5551d9fbc2d9b27|1551270219000|1545054232000; __utma=51854390.1451908785.1547196330.1547196330.1551270221.2; __utmb=51854390.0.10.1551270221; __utmc=51854390'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-feed.feed-item').items()
for i in range(10):
    print(next(items))
# for index,item in enumerate(items):
#     print(item)
    # questions = item.find('h2').text()
    # author = item.find('.author-link-line').text()
    # answer = pq(item.find('.content').html()).text()
    # print(answer, questions, author)
    # with open('explore.txt','a',encoding='utf-8') as f:
    #
    #     f.write("\n".join([questions,author,answer]))
    #     f.write('\n'+"="*50+'\n')
