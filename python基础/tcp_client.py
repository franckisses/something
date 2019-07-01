#_*_coding:utf-8_*_

from socket import *

sockfd = socket(AF_INET,SOCK_STREAM)

sockfd.connect(('127.0.0.1',8590))

data = input('please enter your message:')

sockfd.send(data.encode())

data = sockfd.recv(1024).decode()

print(data)

sockfd.close()

