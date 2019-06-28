# 这是关于字典的练习

# 创建字典
adict = {'name':'bob','age':23}

# 通过dict工厂方法创建字典
adict = dict((['name','bob'],['age',23]))
print(adict)

# 通过fromkeys()创建具有相同值得默认字典
cdict_1 = {}.fromkeys(('bob','alice'),23)
print(cdict_1)

# 字典的访问
# 字典没有下标，只能通过对应的键，才能访问对应得值
new_dict = {'bob': 23, 'alice': 23}
print(new_dict['bob'])

new_dict['bob'] = 25
print(new_dict)

new_dict['harry'] = 45
print(new_dict)

# 删除字典的中的键值对，只需要删除字典的键
del new_dict['bob']
print(new_dict)

# 使用clear的方法可以清空字典
# 使用pop()方法可以弹出字典中的元素
print(new_dict.pop('harry'))
print(new_dict)

# 字典操作符
# 使用in not in 判断键是否存在于字典中
dict_2 = {'age':	23,	'name':	'bob'}
if 'name' in dict_2:
    print('ok')
elif 'gender' not in dict_2:   #why not input
    print('fine')
print('ok')

print(len(dict_2))

# 字典的内建方法
# dict.copy():返回字典的（深复制）的一个副本
dict_3 = {'age':23,'name':'bob'}
print(id(dict_3))
# 31183064
dict_4 = dict_3.copy()
print(id(dict_4))
# 37092160

# 字典的内建方法1
# dict.get(key,default=None)
# 对字典中dict中的键key，返回它对应的value，如果字典不存在此键，则返回default的值

dict_5 = {'name':'xiaowang','age':34,'email':'842549758@qq.com'}
response = dict_5.get('age','its none')
print(response)

# 字典的内建方法2
# dict.setdefault(key.default=None)
# 如果字典中不存在key值，由dict[key]=default为他赋值
print(dict_5)
dict_5.setdefault('gender','man')
print(dict_5)

# 字典内建方法
# dict.items() 返回一个包含中（键，值）对元祖的列表
dict_6 = {'name':'xiaogang','age':34,'gender':'man'}
name = dict_6.items()
for i in name:
    print(i)
# dict.keys() 返回一个包含字典中键的列表
dict_7 = {'name':'xiaogang','age':34,'gender':'man'}
key_items = dict_7.keys()
print(key_items)
for o in  key_items:
    print(o)
# dict.values() 返回一个包含字典中所有值的列表
dict_8 = {'name':'xiaogang','age':34,'gender':'man'}
dict_value = dict_8.values()
print(dict_value)
for p in dict_value:
    print(p)
# dict.update(dict2) 将字典dict2的键值对添加到dict
dict_9 = {'name':'xiaogang','age':34,'gender':'man'}
dict_0 = {'hobby':'football'}
dict_9.update(dict_0)
print(dict_9)
