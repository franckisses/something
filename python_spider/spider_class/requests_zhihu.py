# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:49:32 2018

@author: gongyan
"""

import requests
import re

#headers = {
#        "User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
#        'Cookie':'_zap=2cb15c64-c1c0-432b-8237-d836d4073978; d_c0="AHBk0YhvUw6PTuxRKjC_pVafVMgSuSyNe1Q=|1538897442"; _xsrf=FYPmgvPsWIR2bp7pAQ9JGoe9nMdoj7L1; capsion_ticket="2|1:0|10:1541336505|14:capsion_ticket|44:OGRkMmJkMzQ5OTQzNGRkMmI3N2UxMjYyYjFkMDI3ZmU=|c3166467d621e26b964eb9cb7dff32642ca0969f97a6f7642a74625038097a3c"; r_cap_id="ZWFhODA1NGM5MWVhNDhmNDgzMjRkZjQyMjYwODY3ZjE=|1541336509|bd4d8261ecf6b476347d447612af3500ad930037"; cap_id="NWY3ODUyZGYzNTViNDllYzg5NTA0M2E1ZDgyMzNkYjM=|1541336509|8ba93f905928ae04ac1924ba24d51bfe4c8eaee9"; l_cap_id="NjZjYzRlNDM0MjA2NGE0YmE1MDBhY2VmNmFkZDkzODY=|1541336509|b5faab523a7ef1c34a59e2a06b01735d6e7c642f"; z_c0=Mi4xdzloVkFBQUFBQUFBY0dUUmlHOVREaGNBQUFCaEFsVk54enZNWEFCSm9iRXRNNFFHMVpldUt4S2cwanREbEhqVzl3|1541336519|4b99cf487e81a50d924154febce7c94962bba0bd; tst=r; q_c1=0f90d5418cb645209a257ab1e05eed4a|1541667273000|1541667273000; __utma=51854390.1679093445.1541667268.1541667268.1541667268.1; __utmz=51854390.1541667268.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20140501=1^3=entry_date=20140501=1; tgw_l7_route=c919f0a0115842464094a26115457122'

#        }
#r = requests.get('https://www.zhihu.com/',headers=headers)
#print(r.text)
#pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
#title = re.findall(pattern,r.text)
#print(r.text)


#cookieJar的应用
cookie = '_zap=2cb15c64-c1c0-432b-8237-d836d4073978;\
 d_c0="AHBk0YhvUw6PTuxRKjC_pVafVMgSuSyNe1Q=|1538897442";\
 _xsrf=FYPmgvPsWIR2bp7pAQ9JGoe9nMdoj7L1;\
 capsion_ticket="2|1:0|10:1541336505|14:capsion_ticket|\
 44:OGRkMmJkMzQ5OTQzNGRkMmI3N2UxMjYyYjFkMDI3ZmU=|\
 c3166467d621e26b964eb9cb7dff32642ca0969f97a6f7642a74625038097a3c";\
 r_cap_id="ZWFhODA1NGM5MWVhNDhmNDgzMjRkZjQyMjYwODY3ZjE=|1541336509|\
 bd4d8261ecf6b476347d447612af3500ad930037";\
 cap_id="NWY3ODUyZGYzNTViNDllYzg5NTA0M2E1ZDgyMzNkYjM=|1541336509|\
 8ba93f905928ae04ac1924ba24d51bfe4c8eaee9"; \
 l_cap_id="NjZjYzRlNDM0MjA2NGE0YmE1MDBhY2VmNmFkZDkzODY=|1541336509|b5faab523a7ef1c34a59e2a06b01735d6e7c642f"; z_c0=Mi4xdzloVkFBQUFBQUFBY0dUUmlHOVREaGNBQUFCaEFsVk54enZNWEFCSm9iRXRNNFFHMVpldUt4S2cwanREbEhqVzl3|1541336519|4b99cf487e81a50d924154febce7c94962bba0bd; tst=r; q_c1=0f90d5418cb645209a257ab1e05eed4a|1541667273000|1541667273000; __utma=51854390.1679093445.1541667268.1541667268.1541667268.1; __utmz=51854390.1541667268.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20140501=1^3=entry_date=20140501=1; \
tgw_l7_route=156dfd931a77f9586c0da07030f2df36'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
jar = requests.cookies.RequestsCookieJar()

response = requests.get('http://www.zhihu.com',cookies = jar,headers=headers )
print(response.text)