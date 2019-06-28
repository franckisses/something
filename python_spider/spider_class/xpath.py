# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:42:07 2018

@author: gongyan
"""
from lxml import etree

text = """
<dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c" alt="霸王别姬" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
        <p class="star">
                主演：巩俐,吕齐,童弟
        </p>
<p class="releasetime">上映时间：1993-01-01</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>        
    </div>
      </div>
    </div>
                </dd>
                <dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/1297" title="肖申克的救赎" class="image-link" data-act="boarditem-click" data-val="{movieId:1297}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p0.meituan.net/movie/283292171619cdfd5b240c8fd093f1eb255670.jpg@160w_220h_1e_1c" alt="肖申克的救赎" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1297" title="肖申克的救赎" data-act="boarditem-click" data-val="{movieId:1297}">肖申克的救赎</a></p>
        <p class="star">
                主演：乔·劳格诺,斯科特·曼,约翰·霍顿
        </p>
<p class="releasetime">上映时间：1994-10-14(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
"""

html = etree.HTML(text)

#result = etree.tostring(html)
print(html.xpath('//p[2]/text()'7))
