# -*- encoding: utf-8 -*-
'''
@File    :   fft.py
@Time    :   2019/04/25 16:45:48
@Author  :   franck 
@Version :   1.0
@Contact :   franck_gxu@outlook.com
@License :   (C)Copyright 2019-2025, franck
@Desc    :   machineLearining test!
'''

# here put the import lib

# 将每一列的数据将所

from __future__ import unicode_literals
import numpy as np

raw_samples  = np.array(
    [[3, -1.5, 2, -5.4],
    [0, 4, -0.3, 2.1],
    [1, 3.3, -1.9, -4.3]]
)
print(raw_samples)
print(raw_samples.mean(axis=0))
print(raw_samples.std(axis=0))
std_samples = raw_samples.copy()
for col in std_samples.T:
    print(col)



