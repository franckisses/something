#_*_encode:utf-8_*_

from socket import *
import sys,os
import time

# define the download directory
file_path = "../python2/"


class TftpServer(object):                      #define a class
    def __init__(self,sockfd):
        self.sockfd = sockfd                   # initialization

    def do_list(self):                         # this method is for list the file of directory
        self.sockfd.send(b'L')  #send a signal for look for directory ,in the transfor must be bytes
        data = self.sockfd.recv(1024).decode() #recv() define the accept size of data
        if data =="OK":                        # if receive OK ,then  start receive the data
            data = self.sockfd.recv(4096).decode()
            files = data.split("#")           # use the '#' to split the receive data
            for file in files:                # show all of the the list of file
                print(file)
            print("%%%%%%the file show over%%%%%%%")
        else:
            #we have no recevie data
            print(data)


    def do_get(self,filename):
        self.sockfd.send(("G "+filename).encode()) #send a signal G to recognize get file
        data = self.sockfd.recv(1024).decode()
        if data == "OK":  # this signal is for recognize the state
            with open(file_path+filename,'w') as f:  #start save file
                while True:
                    data = self.sockfd.recv(1024).decode()
                    if data == "##": # recognize end of file
                        break
                    f.write(data)  #put the data write the file
            print("%s download finish"%filename)  #finish the file

    def do_put(self,filename): # this method is for push the file to server
        try:
            f = open(file_path+filename,"rb")  #recognize the file is exist!
        except:
            print("the file is not exist!")  #print the state of file
            return
        self.sockfd.send(("P "+filename).encode())   #send the filename to server
        data = self.sockfd.recv(1024).decode()   #recv the state of server
        if data == "OK":
            for line in f:
                self.sockfd.send(line) # line to line send the data to server
            time.sleep(0.1)
            self.sockfd.send(b"##")  #send the signal to server
            f.close() #close the file
            print("%s the file is upload over"%filename)  #print upload over signal
        else:
            print(data)  #print the wrong reason



    def show_current(self):    # this method is for show the current file
        file_list = os.listdir(file_path) #show the file of directory
        if not file_list:
            return "the file is empty"
        for file in file_list:
            print(file) #show the file of

    def do_quit(self):
        self.sockfd.send(b"Q")



def main():
    host = "127.0.0.1"  #remote server ipaddress
    port = 8599
    addr = (host,port)

    sockfd = socket()
    sockfd.connect(addr)

    # tftp object
    tftp = TftpServer(sockfd)







    while True:
        print("=========choice option============")
        print("=========list remote===============")
        print("=========list current==============")
        print("=========  get file  ==============")
        print("=========  put file  ==============")
        print("=========  quit      ==============")
        print("===================================")

        cmd = input("please enter commend:")
        if cmd.split()[-1] == 'current':
            tftp.show_current()
        elif cmd.split(" ")[-1] =='remote':
            tftp.do_list()
        elif cmd[:3] == 'get':
            filename =cmd.split(" ")[-1]
            print(filename)
            tftp.do_get(filename)
        elif cmd[:3] == "put":
            filename =cmd.split(" ")[-1]
            print(filename)
            tftp.do_put(filename)
        elif cmd.strip() == "quit":
            tftp.do_quit()
            sockfd.close()
            sys.exit()
        else:
            print("choice a options!")
            continue

if __name__ == '__main__':
    main()
