
#学生问题：
# a = 'ab c d e'
a = input('请输入字符串：')
n = 0
for s in a:
    if s == ' ':
        n +=1
    print('x--->',s,n)