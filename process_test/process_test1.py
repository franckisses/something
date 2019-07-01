# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      process_test1
   Description :    多进程
   Author :         gongyan
   Date：           2019/2/28
   Change Activity: 2019/2/28 6:06
-------------------------------------------------
"""

from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start();
    p.join()
    print('Child process end.')