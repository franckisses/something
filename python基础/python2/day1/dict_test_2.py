# 编写unix2dos的程序
# 1.windows文本文件的行结束标志是 \r\n
# 2.类unix文本文件的行结束标志是\n
# 3.编写程序将unix文本文件格式转换为windows文本文件的格式

# 先将文本文件读取出来 再用替换\r\n为\n
with open("old.txt","r") as f:
    a = f.readlines()
    for i in a:
        i.replace("\r\n","\n")
        print(i)




