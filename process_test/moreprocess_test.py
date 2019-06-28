# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      moreprocess_test
   Description :
   Author :         gongyan
   Date：           2019/2/28
   Change Activity: 2019/2/28 6:13
-------------------------------------------------
"""

from multiprocessing import Pool
import os, time, random
import  requests

def long_time_task(name):
    start = time.time()
    print(name)
    response = requests.get('http://www.httpbin.org/get')
    # print(response.text)
    print(time.time()-start)

if __name__=='__main__':
    parentstart = time.time()
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    print(time.time()-parentstart)