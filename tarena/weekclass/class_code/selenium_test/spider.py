# -*-coding：utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from urllib.parse import quote

browser = webdriver.Chrome()
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)
#
wait = WebDriverWait(browser, 10)
KEYWORD= 'iphone'

def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)


        time.sleep(100000)

    #     if page > 1:
    #         input = wait.until(
    #             EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
    #         submit = wait.until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
    #         input.clear()
    #         input.send_keys(page)
    #         submit.click()
    #     wait.until(
    #         EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
    #     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
    #     get_products()
    # except TimeoutException:
    #     index_page(page)


# def get_products():
#     """
#     提取商品数据
#     """
#     html = browser.page_source
#     print(html)
    # doc = pq(html)
    # items = doc('#mainsrp-itemlist .items .item').items()
    # for item in items:
    #     product = {
    #         'image': item.find('.pic .img').attr('data-src'),
    #         'price': item.find('.price').text(),
    #         'deal': item.find('.deal-cnt').text(),
    #         'title': item.find('.title').text(),
    #         'shop': item.find('.shop').text(),
    #         'location': item.find('.location').text()
    #     }
    #     print(product)
        


def main():
    """
    遍历每一页
    """
    for i in range(1, 10 + 1):
        index_page(i)
    browser.close()


if __name__ == '__main__':
    main()
