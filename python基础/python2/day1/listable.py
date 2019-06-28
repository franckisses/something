
# 可变集合：set
# 不可变集合：frozenset
# 集合支持用in 和 not in 操作符检查成员
# 能够通过len()检查集合大小
# 能够使用for迭代集合成员
# 不能去切片，没有键
#
# | 联合，取并集
# & 取交集
# - 差补
# 集合的内建方法
# set.add() 添加成员
# set.update() 批量添加成员
# set.remove() 移除成员


s1 = set("hello")
print(s1)
# s1.issubset(t) 如果s是t的子集，则返回True，否则返回Fales
# s1.issuperset(t) 如果t是s的超集，则返回True，否则返回False
# s1.union(t) 返回一个新的集合，该集合是s和t的并集
# s1.intersection(t)  返回一个新集合，该集合是s和t的交集
# s1.difference(t)    返回一个新的集合，该集合是s的成员，但不是t的成员

# datetime.today()：返回一个表示当前本地时间的datetime对象
# datetime.now([tz])：返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间
# datetime.strptime(date_string, format)：将格式字符串转换为datetime对象
# datetime.ctime(datetime对象)：返回时间格式字符串
# datetime.strftime(format)：返回指定格式字符串
