#-*- coding: UTF-8 -*-
import os
import socket
def IsOpen(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        print('%d is open' % port)
        return True
    except:
        print('%d is down' % port)
        return False
if __name__ == '__main__':
    IsOpen('172.16.119.30',3389)