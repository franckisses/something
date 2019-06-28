from bs4 import BeautifulSoup


#this file is for test BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,"lxml")

#将代码格式化8
# print(soup.prettify())


# 1.tag实例soup.标签a/p,代表遍历到第一个a标签或者p标签
# print(type(soup.a))
# 匹配即停止
# print(soup.a)


# 获取内容：
# title_text = soup.title.string
# title_text1 = soup.title.get_text()
# title_text2 = soup.title.text

# print(title_text)
# print(title_text1)
# print(title_text2)

#name实例
#tag实例可以转化为name实例
# a = soup.title
# print(a.name)

# 选取属性
# b = soup.a.attrs
# print(b['href'])
# print(b['class'][0])
# print(b['id'])

# 选取多个属性
# 返回值是一个列表，将所有的a标签返回
# c = soup.find_all('a')
# print(c)

# c = soup.find_all(name='a',attrs={'href':'http://example.com/tillie'})
# print(c)
# 

# contents属性
# 返回的结果是一个列表形式。可以将元素中的节点以及文本都匹配出来。
# print('#'*50)
# print(soup.p.contents)


#父节点以及祖先节点parent，patents
# p_parent = soup.p.parent
# print(p_parent)

# p_parents = soup.p.parents
# print(p_parents)
# print(list(enumerate(p_parents)))

# 查找兄弟节点
# next_sibling 查找下一个兄弟节点
# previous_sibling 查找上一个兄弟节点
# next_siblings  查找所有后面的节点
# previous_siblings 查找所有的前面节点


# css选择器
# print(soup.select('p a'))
print(soup.select('.sister'))
