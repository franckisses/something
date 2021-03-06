import requests
from bs4 import BeautifulSoup
import csv,time

def get(page, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    text = response.text
    soup = BeautifulSoup(text, "lxml")
    pagesource = []
    for i in soup.select('#myTable04 tr'):
        if not i.select('td'):
            print('准备开始下载第%s页数据' % page)
        else:
            # 这是编号
            num = i.select('td')[0].get_text()
            # 股票代码
            stock_code = i.select('td')[1].get_text()
            # 股票名称
            name = i.select('td')[2].get_text()
            # 公司名称
            company = i.select('td')[3].get_text()
            # 省份
            province = i.select('td')[4].get_text()
            # 城市
            city = i.select('td')[5].get_text()
            # 收入
            income = i.select('td')[6].get_text()
            # 利润
            profit = i.select('td')[7].get_text()
            # 员工人数
            employees = i.select('td')[8].get_text()
            # 上市时间
            IpoTime = i.select('td')[9].get_text()
            # 行业
            industry = i.select('td')[12].get_text()
            # 产品类型
            product_type = i.select('td')[13].get_text()
            # 主营业务
            mainBusiness = i.select('td')[14].get_text()
            #在这里进行数据结构化。将数据存储为列表形式的
            a= [num,stock_code,name,company,province,city,income,profit,employees,IpoTime,industry,product_type,mainBusiness]
            with open('data.csv',"a+",newline="") as f:
                writer = csv.writer(f)
                writer.writerow(a)

if __name__ == '__main__':
    row0 = [u'编号', u'股票代码', u'股票名称', u'公司名称', u'省份', u'城市',
                u'收入', u'利润', u'员工人数', u'上市时间', u'行业', u'产品类型', u'主营业务']
    with open('data.csv',"a+",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row0)
    for page in range(1, 180):
        url = 'http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum={}#QueryCondition'.format(
            page)
        time.sleep(2)
        data = get(page, url)
        print('第%s页下载成功' % page)
