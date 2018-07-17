#!/usr/bin/python3
# -*- coding: utf-8 -*-
from socket import *


openNum = 0

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        openNum += 1
        print('[+] %d open' % port)
        s.close()
    except:
        print('[-] %d close' % port)
def main():
    setdefaulttimeout(0.1)
    for p in range(1,200):
        portScanner('118.193.95.94',p)

    print('[*] The scan is complete!')
    print('[*] A total of %d open port ' % (openNum))

if __name__ == '__main__':
    main()