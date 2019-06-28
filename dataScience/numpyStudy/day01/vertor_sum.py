#this file is for the numpy test
#此示例用来演示numpy对于多元数组的展示。

import numpy as np
import os
import sys
import datetime as dt

def python_sum(n):
    a = [i**2 for i in range(n)]
    b = [i**3 for i in range(n)]
    c = []
    for i in range(n):
        c.append(a[i]+b[i])
    return c


def numpy_sum(n):
    return np.arange(n) ** 2 + np.arange(n) ** 3



def main(argc,argv,envp):
    n = 100000
    start = dt.datetime.now()
    c = python_sum(n)
    print((dt.datetime.now()-start).microseconds)
    start2 = dt.datetime.now()
    c = numpy_sum(n)
    print((dt.datetime.now()-start2).microseconds)


if __name__ == '__main__':
    sys.exit(main(len(sys.argv),sys.argv,os.environ))

