# -*- coding:utf-8 -*-
import json,time
import sys
import requests
import re


class MyWeahter:
    '''我的天气类'''
    __w = ''

    def __init__(self, city):
        self.city = city

    def get_weather(self):
        '''获取天气'''
        addr = self.city
        if addr == 'E' or addr == 'e' or not addr:
            sys.exit(0)  # 关闭程序
        # 获取天气json
        weatherJsonUrl = "http://wthrcdn.etouch.cn/weather_mini?city=%s" % addr
        #以get的方式提交
        response = requests.get(weatherJsonUrl)
        try:
            print(response.raise_for_status())
        except:
            print('网址请求出错')
        weatherData = json.loads(response.text)
        print(weatherData)
        global __w
        __w = weatherData['data']
        return __w

    #获取今天天气数组，并返回为列表
    def today(self):
        weather = __w['forecast']
        __date = weather[0]['date']
        __high = weather[0]['high']
        __high=re.findall(r'\d+℃$',__high)[0]
        __low = weather[0]['low']
        __low=re.findall(r'\d+℃$',__low)[0]
        __weather =weather[0]['type']
        __wendu = __w['wendu'] + '℃ '
        __fx = weather[0]['fengxiang'] + ":" + re.findall(r'\d?[-<>]\d+\S', weather[0]['fengli'])[0]
        return [__date,__wendu, __weather,'%s/%s '%(__low,__high),__fx]
    #传参形式获取后续四天天气数组，并返回为列表
    def otherday(self,day):
        weather = __w['forecast']
        __date = weather[day]['date']
        __high = weather[day]['high']
        __high = re.findall(r'\d+℃$', __high)[0]
        __low = weather[day]['low']
        __low = re.findall(r'\d+℃$', __low)[0]
        __weather = weather[day]['type']+"  "
        __fx=weather[day]['fengxiang']+":"+re.findall(r'\d?[-<>]\d\S',weather[day]['fengli'])[0]
        # print(__fx)
        return [__date,__weather, '%s/%s '%(__low,__high),__fx]
    #返回当前城市，以及友情提示
    def other(self):
        city = __w['city']
        ganmao = __w['ganmao']
        return [city, ganmao]

if __name__ == '__main__':
    a = MyWeahter('厦门')
    a.get_weather()
#     weather = a.today()
#     daysinfo=a.otherday(1)
#     print(weather)
#     print(daysinfo)
# #     msg='%d年%d月%s,%s,温度%s风力%s.'%(time.localtime()[0],time.localtime()[1],weather[0],weather[2],weather[3],weather[4])
# #     print(msg)
# #     tm=a.otherday(1)
#     print(",".join(tm))
#     tm1=a.otherday(2)
#     tm2=a.otherday(3)
#     print(",".join(tm1))
#     print(",".join(tm2))

    # ..   %s，温度%d风力%s
    # print(tm)
    # print(tm1)
    # print(tm2)
    # print(",".join(a.other()))
