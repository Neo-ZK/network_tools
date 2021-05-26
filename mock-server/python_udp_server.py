#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import logging
import struct
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 5002))

print('Bind UDP on 5002...')

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='server.log', level=logging.DEBUG, format=LOG_FORMAT)

def byte42int(str):
    arr = struct.unpack('>BBBB', str)
    res = (arr[0] << 24) | (arr[1] << 16) |(arr[2] << 8) |arr[3]
    return res

while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    if data:
        seq = byte42int(data[0:4])
        rt =  time.time() - byte42int(data[4:8])
        print(rt)
        print('Received from %s, len is %d, seq is %d, rt is %f' % (addr, len(data), seq, rt))
        logging.debug('Received from %s, len is %d, seq is %d, rt is %f' % (addr, len(data), seq, rt))
        sent = s.sendto(data, addr)
