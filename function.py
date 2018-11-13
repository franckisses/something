# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     function
   Description :
   Author :       gongyan
   date：          2018/10/11
   Change Activity:2018/10/11 10:40:
-------------------------------------------------
"""
def build_phone(brand,model):
    print("接到生产%s手机的通知"%brand)
    print("正在组装%s%s"%(brand,model))
    print("生产完毕")
    return '您的新手机%s%s到了'%(brand,model)

print(build_phone("iphone",'8'))