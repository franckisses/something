# ���ǹ����ֵ����ϰ

# �����ֵ�
adict = {'name':'bob','age':23}

# ͨ��dict�������������ֵ�
adict = dict((['name','bob'],['age',23]))
print(adict)

# ͨ��fromkeys()����������ֵͬ��Ĭ���ֵ�
cdict_1 = {}.fromkeys(('bob','alice'),23)
print(cdict_1)

# �ֵ�ķ���
# �ֵ�û���±ֻ꣬��ͨ����Ӧ�ļ������ܷ��ʶ�Ӧ��ֵ
new_dict = {'bob': 23, 'alice': 23}
print(new_dict['bob'])

new_dict['bob'] = 25
print(new_dict)

new_dict['harry'] = 45
print(new_dict)

# ɾ���ֵ���еļ�ֵ�ԣ�ֻ��Ҫɾ���ֵ�ļ�
del new_dict['bob']
print(new_dict)

# ʹ��clear�ķ�����������ֵ�
# ʹ��pop()�������Ե����ֵ��е�Ԫ��
print(new_dict.pop('harry'))
print(new_dict)

# �ֵ������
# ʹ��in not in �жϼ��Ƿ�������ֵ���
dict_2 = {'age':	23,	'name':	'bob'}
if 'name' in dict_2:
    print('ok')
elif 'gender' not in dict_2:   #why not input
    print('fine')
print('ok')

print(len(dict_2))

# �ֵ���ڽ�����
# dict.copy():�����ֵ�ģ���ƣ���һ������
dict_3 = {'age':23,'name':'bob'}
print(id(dict_3))
# 31183064
dict_4 = dict_3.copy()
print(id(dict_4))
# 37092160

# �ֵ���ڽ�����1
# dict.get(key,default=None)
# ���ֵ���dict�еļ�key����������Ӧ��value������ֵ䲻���ڴ˼����򷵻�default��ֵ

dict_5 = {'name':'xiaowang','age':34,'email':'842549758@qq.com'}
response = dict_5.get('age','its none')
print(response)

# �ֵ���ڽ�����2
# dict.setdefault(key.default=None)
# ����ֵ��в�����keyֵ����dict[key]=defaultΪ����ֵ
print(dict_5)
dict_5.setdefault('gender','man')
print(dict_5)

# �ֵ��ڽ�����
# dict.items() ����һ�������У�����ֵ����Ԫ����б�
dict_6 = {'name':'xiaogang','age':34,'gender':'man'}
name = dict_6.items()
for i in name:
    print(i)
# dict.keys() ����һ�������ֵ��м����б�
dict_7 = {'name':'xiaogang','age':34,'gender':'man'}
key_items = dict_7.keys()
print(key_items)
for o in  key_items:
    print(o)
# dict.values() ����һ�������ֵ�������ֵ���б�
dict_8 = {'name':'xiaogang','age':34,'gender':'man'}
dict_value = dict_8.values()
print(dict_value)
for p in dict_value:
    print(p)
# dict.update(dict2) ���ֵ�dict2�ļ�ֵ����ӵ�dict
dict_9 = {'name':'xiaogang','age':34,'gender':'man'}
dict_0 = {'hobby':'football'}
dict_9.update(dict_0)
print(dict_9)
