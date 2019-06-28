# -*-coding: utf-8 -*-
from wxpy import *

# 初始化机器人，用于扫码登录

bot = Bot()


# 用于查找朋友，是否存在Sweetie的好友

myfrind = bot.friends('Sweetie',sex=FEMALE)
print(myfrind)

# 发送消息：
myfriend.send('I love you!')
# 发送图片
myfrind.send('wechat/1.jpg')
