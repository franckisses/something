# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     class_xpath
   Description :   this is for xpath show！
   Author :       gongyan
   date：          2018/12/20
   Change Activity:2018/12/20 9:28:
-------------------------------------------------
"""

html = """
<html>
    <tbody>
        <tr class="h">
            <td class="l" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
        <tr class="even">
            <td class="l square">
                <a target="_blank" >30359-存储后台开发高级工程师</a>
                <img class="large" src="http://www.bing.com/az/hprichbg/rb/PragueChristmas_EN-CN8649790921_800x480.jpg" >           
            </td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2018-12-20</td>
        </tr>
        <tr class="odd">
            <td class="l square">
                <a target="_blank" >30359-大数据平台web前端开发工程师</a>
                <img class="large" src="http://www.bing.com/az/hprichbg/rb/PragueChristmas_EN-CN8649790921_800x480.jpg" >
            </td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2018-12-20</td>
        </tr>
    </tbody>
</html>
"""

from lxml import etree

html = etree.HTML(html)
# print(html)
print(html.xpath('//a/text()'))
print(html.xpath('//img/@src'))