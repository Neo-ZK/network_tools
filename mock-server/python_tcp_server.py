#!/usr/bin/python
#****************************************************************#
# ScriptName: python_server.py
# Author: $SHTERM_REAL_USER@alibaba-inc.com
# Create Date: 2021-04-26 14:00
# Modify Author: $SHTERM_REAL_USER@alibaba-inc.com
# Modify Date: 2021-05-06 15:39
# Function: 
#***************************************************************#
from socket import *
from time import ctime
import time

host = '127.0.0.1'
port = 81
ADDR = (host, port)
BUFSIZ = 4096

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.bind(ADDR)
#set the max number of tcp connection
tcpSocket.listen(5)
http_resp_header = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 400\r\n\r\n"
http_resp_body1 = ""
http_resp_body2 = ""
for i in range(0,200):
    http_resp_body1 += "a"
    http_resp_body2 += "b"
while True:
    print('waiting for connection...')
    clientSocket, clientAddr = tcpSocket.accept()
    print('conneted form: %s' %clientAddr[0])

    while True:
        try:
            data = clientSocket.recv(BUFSIZ)
        except IOError as e:
            print(e)
            clientSocket.close()
            break
        if not data:
            break
        print(data)
        clientSocket.send(http_resp_header)
        clientSocket.send(http_resp_body1)
        #time.sleep(2)
        clientSocket.send(http_resp_body2)
    clientSocket.close()
tcpSocket.close()
