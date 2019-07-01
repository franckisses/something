# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     asyncio_test
   Description :
   Author :       gongyan
   date：          2018/12/22
   Change Activity:2018/12/22 1:17:
-------------------------------------------------
"""
import asyncio
import aiohttp  #异步爬取网页的库
import time

start = time.time()

async def get(url):
    session = aiohttp.ClientSession()  #通过构建session对象来请求网页内容
    response = await session.get(url)  #通过get方法来请求网页
    result = response.status           #查看网页的响应码
    print(result)
    session.close()
    return response


async def request():
    url = 'http://www.baidu.com'
    await get(url)


tasks = [asyncio.ensure_future(request()) for _ in range(100)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)