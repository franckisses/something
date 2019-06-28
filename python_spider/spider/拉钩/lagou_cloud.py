# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     lagou_cloud
   Description :
   Author :       gongyan
   date：          2019/2/12
   Change Activity:2019/2/12 16:26:
-------------------------------------------------
"""
import requests


def get_page(url):
    headers= {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        # 'Cookie': '_ga=GA1.2.1017063746.1544443602; user_trace_token=20181210200641-0defdcb2-fc74-11e8-8f6b-525400f775ce; LGUID=20181210200641-0defe22b-fc74-11e8-8f6b-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167980332db7bf-050c5b06071ff9-3a3a5d0c-1049088-167980332dcbc4%22%2C%22%24device_id%22%3A%22167980332db7bf-050c5b06071ff9-3a3a5d0c-1049088-167980332dcbc4%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pc%22%7D%7D; LG_LOGIN_USER_ID=23a3ffee4d55ba289a75f15a2125b8381e6f7d0c38ce4d73; JSESSIONID=ABAAABAAADEAAFIBB9ACFAF9656F963CCD29BDBDB2C2D3B; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549959138; _gid=GA1.2.59601891.1549959138; LGSID=20190212161221-ebd39412-2e9d-11e9-8170-5254005c3644; index_location_city=%E5%8C%97%E4%BA%AC; SEARCH_ID=780cc7f6ba834cc1b90e73e828d09285; TG-TRACK-CODE=jobs_similar; _gat=1; LGRID=20190212164320-4032360a-2ea2-11e9-8171-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549960998',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh,zh-CN;q=0.9,en;q=0.8',
        # 'Cache-Control': 'max-age=0',
        # 'Connection': 'keep-alive'
    }
    response = requests.get(url,headers=headers)
    print(response.status_code)
    # print(response.text)
    jod_detail =


if __name__ == '__main__':
    url = "https://www.lagou.com/jobs/5393593.html"
    get_page(url)