# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     newdata
   Description :
   Author :       gongyan
   date：          2018/12/17
   Change Activity:2018/12/17 15:14:
-------------------------------------------------
"""

import pandas as pd

data = pd.read_excel('datasource.xlsx',sheet_name='Sheet1')
print(data.head())
