# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      yibu
   Description :     
   Author :         gongyan
   Date：           2019/2/28
   Change Activity: 2019/2/28 6:26
-------------------------------------------------
"""
import time

import asyncio
import requests


start  = time.time()

async def request(_):
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

tasks = [asyncio.ensure_future(request(_)) for _ in range(50)]
print('Tasks:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task Result:', task.result())

print(time.time()-start)