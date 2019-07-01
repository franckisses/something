# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      re_test
   Description :     
   Author :         gongyan
   Date：           2019/2/27
   Change Activity: 2019/2/27 9:02
-------------------------------------------------
"""
import re
text = """
<a class="item" href="http://bing.plmeizi.com/show/997" target="_blank">
    <div><img src="http://bimgs.plmeizi.com/images/bing/2019/AbstractSaltBeds_ZH-CN8351691359_1920x1080.jpg-listpic" alt="鸟瞰尾矿池，澳大利亚 (&copy; Amazing Aerial/Offset)" ></div>
    <p>鸟瞰尾矿池，澳大利亚 (&copy; Amazing Aerial/Offset) (20190218)</p>
</a>
<a class="item" href="http://bing.plmeizi.com/show/996" target="_blank">
    <div><img src="http://bimgs.plmeizi.com/images/bing/2019/GBBC_ZH-CN4481989355_1920x1080.jpg-listpic" alt="德克萨斯州山区的黑冠山雀 (&copy; Rolf Nussbaumer/Minden Pictures)" ></div>
    <p>德克萨斯州山区的黑冠山雀 (&copy; Rolf Nussbaumer/Minden Pictures) (20190217)</p>
</a>
<a class="item" href="http://bing.plmeizi.com/show/995" target="_blank">
    <div><img src="http://bimgs.plmeizi.com/images/bing/2019/PangolinDay_ZH-CN4393242380_1920x1080.jpg-listpic" alt="戈龙戈萨国家公园的南非穿山甲，莫桑比克 (&copy; Jen Guyton/Minden Pictures)" ></div>
    <p>戈龙戈萨国家公园的南非穿山甲，莫桑比克 (&copy; Jen Guyton/Minden Pictures) (20190216)</p>
</a>
"""

pattern = re.compile('<a.*?item.*?_blank.*?src=(>*?)></div>')
print(re.findall(pattern,text))