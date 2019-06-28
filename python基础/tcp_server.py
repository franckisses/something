from socket import *

sockfd = socket(AF_INET,SOCK_STREAM)


sockfd.bind(('0.0.0.0',8590))

sockfd.listen(5)
conn,addr = sockfd.accept()

data = conn.recv(1024)
print(data.decode())

conn.send("glad receive your message".encode())

conn.close()
sockfd.close()