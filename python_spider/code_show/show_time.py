# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     show_time
   Description :
   Author :       gongyan
   date：          2018/11/16
   Change Activity:2018/11/16 10:01:
-------------------------------------------------
"""
from bs4 import BeautifulSoup

some_str = """
<tr class="even">
    <span>腾讯云高级运营经理</span>
    <td>产品/项目类</td>
    <td>1</td>
    <td>深圳</td>
    <td>2018-11-16</td>
</tr>
<tr class="odd">
    <span>企鹅直播运营</span>
    <td>产品类</td>
    <td>1</td>
    <td>北京</td>
    <td>2018-11-16</td>
</tr>
"""
soup = BeautifulSoup(some_str,'lxml')
trs = soup.select('tr')
print(trs)

>>>[<tr class="even">
   <span>腾讯云高级运营经理</span>
   <td>产品/项目类</td>
   <td>1</td>
   <td>深圳</td>
   <td>2018-11-16</td>
   </tr>, <tr class="odd">
   <span>企鹅直播运营</span>
   <td>产品类</td>
   <td>1</td>
   <td>北京</td>
   <td>2018-11-16</td>
   </tr>]





