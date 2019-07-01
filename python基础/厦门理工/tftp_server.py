#_*_encode:utf-8_*_

"""this is a file server"""

from socket import *
import os,sys
import signal
import time

file_path = "../socket_test/"  #define a server file

class TftpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd
#
    def do_list(self):
        # this is show for the file
        file_list = os.listdir(file_path)
        if not file_list:
            self.connfd.send('the file is empty'.encode())
            return
        self.connfd.send(b'OK')
        time.sleep(0.1)

        files = ""
        for file in file_list:
            if file[0] != "." and os.path.isfile(file_path+file):
                files = files + file +"#"
        self.connfd.send(files.encode())

    def do_get(self,filename):
        try:
            fd = open(file_path+filename,'rb')
        except:
            self.connfd.send("the file is not exist!".encode())
            return
        self.connfd.send(b'OK')
        time.sleep(0.1)
        #send file
        try:
            for line in fd:
                self.connfd.send(line)
            fd.close()
        except Exception as e:
            print(e)
        time.sleep(0.1)
        self.connfd.send(b"##")

    def do_put(self,filename):
        try:
            f = open(file_path+filename,'w')
        except:
            self.connfd.send(b"the file can't upload!")
        self.connfd.send(b'OK')
        while True:
            data = self.connfd.recv(1024).decode()
            if data == "##":
                break
            f.write(data)
        f.close()
        print('upload over!')


#access control
def main():
    HOST = '0.0.0.0'
    PORT = 8599
    ADDR = (HOST, PORT)

    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    print("listen the remote.....")

    signal.signal(signal.SIGCHLD,signal.SIG_IGN)




    while True:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit('server quit')
        except Exception as e:
            print(e)
            continue
        print("clent sign in",addr)


        pid = os.fork()         #create father-children process
        if pid < 0:
            print("create child process failed!")
            continue
        elif pid == 0:
            sockfd.close()
            tftp =TftpServer(connfd)
            while True:
                data = connfd.recv(1024).decode()
                if not data:
                    continue
                elif data[0] == "L":
                    tftp.do_list()
                elif data[0] == "G":
                    filename = data.split(' ')[-1]
                    tftp.do_get(filename)
                elif data[0] == "P":
                    filename = data.split(' ')[-1]
                    tftp.do_put(filename)
                elif data[0] == "Q":
                    print('client quit!')
                    sys.exit()
        else:
            connfd.close()
            continue

if __name__ == '__main__':
    main()
