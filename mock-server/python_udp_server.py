#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import logging

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 5002))

print('Bind UDP on 5002...')

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='server.log', level=logging.DEBUG, format=LOG_FORMAT)

while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s, len is %d' % (addr, len(data)))
    logging.debug('Received from %s, len is %d' % (addr, len(data)))
    if data:
        sent = s.sendto(data, addr)
