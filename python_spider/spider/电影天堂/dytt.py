# http://www.dytt8.net/html/gndy/dyzz/index.html

# import requests
# from lxml import etree
#
# url="http://www.dytt8.net/html/gndy/dyzz/index.html"
# header={
# "Cookie": "td_cookie=18446744070634153048; td_cookie=18446744070634105235",
# "Host": "www.dytt8.net",
# "Referer": "http://www.dytt8.net/html/gndy/dyzz/index.html",
# "Upgrade-Insecure-Requests": "1",
# "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
# }
# resp=requests.get(url,headers=header)
# print(resp.status_code)
# print(resp.text)
import requests
from lxml import etree

BASE_DOMAIN = 'http://www.dytt8.net'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Referer': 'http://www.dytt8.net/html/gndy/dyzz/list_23_2.html'
}

def spider():
    url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
    resp = requests.get(url,headers=HEADERS)
    # resp.content�������������ַ���
    # resp.text��û�о������룬Ҳ����unicode�ַ���
    # text���൱������ҳ�е�Դ������
    text = resp.text
    # tree������lxml�������һ�������Ժ�ʹ����������xpath�������Ϳ���
    # ��ȡһЩ��Ҫ��������
    tree = etree.HTML(text)
    print(tree)
#     # xpath/beautifulsou4
#     all_a = tree.xpath("//div[@class='co_content8']//a")
#     for a in all_a:
#         title = a.xpath("text()")[0]
#         href = a.xpath("@href")[0]
#         if href.startswith('/'):
#             detail_url = BASE_DOMAIN + href
#             crawl_detail(detail_url)
#             break
#
# def crawl_detail(url):
#     resp = requests.get(url,headers=HEADERS)
#     text = resp.content.decode('gbk')
#     tree = etree.HTML(text)
#     create_time = tree.xpath("//div[@class='co_content8']/ul/text()")[0].strip()
#     imgs = tree.xpath("//div[@id='Zoom']//img/@src")
#     # ��Ӱ����
#     cover = imgs[0]
#     # ��Ӱ��ͼ
#     screenshoot = imgs[1]
#     # ��ȡspan��ǩ�����е��ı�
#     infos = tree.xpath("//div[@id='Zoom']//text()")
#     for index,info in enumerate(infos):
#         if info.startswith("���ꡡ����"):
#             year = info.replace("���ꡡ����","").strip()
#
#         if info.startswith("�򶹰�����"):
#             douban_rating = info.replace("�򶹰�����",'').strip()
#             print(douban_rating)
#
#         if info.startswith("����������"):
#             # �ӵ�ǰλ�ã�һֱ���������
#             actors = [info]
#             for x in range(index+1,len(infos)):
#                 actor = infos[x]
#                 if actor.startswith("��"):
#                     break
#                 actors.append(actor.strip())
#             print(",".join(actors))


if __name__ == '__main__':
    spider()