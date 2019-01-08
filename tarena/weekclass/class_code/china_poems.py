# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     xpath_show
   Description :
   Author :       gongyan
   date：          2019/1/4
   Change Activity:2019/1/4 17:02:
-------------------------------------------------
"""
import requests
from lxml import etree
import sys
import io,json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='GB18030')


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    title = html.xpath('/html/body/div[2]/div[1]/div/div[1]/p[1]/a/b/text()')
    dynasty = html.xpath('/html/body/div[2]/div[1]/div/div[1]/p[2]/a[1]/text()')
    auther = html.xpath('/html/body/div[2]/div[1]/div/div[1]/p[2]/a[2]/text()')
    content = html.xpath('//div[@class="contson"]')
    for i in range(10):
        p_tags = content[i].xpath('./p')
        poems = ""
        if not p_tags:
            print(content[i].xpath('./text()'))
        else:
            p_num = len(p_tags)
            for num in range(p_num):
                # print('ok')
                print('ok',content[i].xpath('./p[{}]/text()'.format(num+1)))




    # for i in range(10):
    #     if content[i].xpath('./text()'):
    #         print(content[i].xpath('./text()'))
    #     elif content[i].xpath('./p/text()'):
    #         print(content[i].xpath('./p/text()'))

        # print(poems)
        # items['poems'] = ",".join(poems).strip()
        # items['title'] = title[i]
        # items['auther'] = auther[i]
        # items['dynasty'] = dynasty[i]
        # with open('poems.json','a+') as f:
        #     f.write(json.dumps(items,ensure_ascii=False)+'\n')


if __name__ == '__main__':
    for i in range(1,20):
        url = "https://www.gushiwen.org/default_{}.aspx"
        get_page(url.format(i))
        break