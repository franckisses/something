import requests
from lxml import etree
import json
import time

def request_list_page():
    url = ""
    headers = {
        "User-Agent":"",
        "Referer":'',
        "Cookie":"",
        "Origin":"",
        "X-Anit-Forge-Code":0,
        "X-Anit-Forge-Token":"",
        "X-Requested-With":"",
    }
    data = {
        "first":"false",
        "pn":1,
        "kd":"python"
    }
    for x in range(1,14):
        data["pn"] = x
        response = requests.post(url,headers = headers,data = data)
        time.sleep(1)
        result = response.json()
        positions = result['content']['positonResult']['result']
        for position in positions:
            positionId = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html'%positionId
            parse_position_detail(position_url)
            break
        break

def parse_position_detail(url):
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    position_name = html.xpath("//spam[@class='name']/text()")[0]
    job_request_spans = html.xpath("//dd[@class='job_request']//span")
    salary = job_request_spans[0].xpath(".//text()")[0].strip()
    city = job_request_spans[1].xpath(".//text()")[0].strip()
    city = re.sub(r"[\s/]","",city)
    work_years = job_request_spans[2].xpath(".//text()")[0].strip()
    work_years = re.sub(r"[\s/]","",work_years)
    education = job_request_spans[3].xpath(".//text()")[0].strip()
    education = re.sub(r"[\s/]", "", education)
    fulltime = job_request_spans[4].xpath(".//text()")[0].strip()
    fulltime = re.sub(r"[\s/]", "", fulltime)

    detail = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()



    print(response.text)


def main():
    request_list_page()

if __name__ =="__mian__":
    main()