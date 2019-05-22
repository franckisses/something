

a = open('2.txt','r')
s = a.readlines()
for i in s:
	print(i)
	print(type(i),len(i))
a.close()
