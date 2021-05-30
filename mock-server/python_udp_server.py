#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import logging
import struct
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('', 5002))

print('Bind UDP on 5002...')

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='server.log', level=logging.DEBUG, format=LOG_FORMAT)

def byte82int(str):
    arr = struct.unpack('>BBBBBBBB', str)
    res = (arr[0] << 56) | (arr[1] << 48) |(arr[2] << 40) | (arr[3] << 32) | (arr[4] << 24) | (arr[5] << 16) |(arr[6] << 8) | arr[7]
    return res

def get_curr_time_ms():
    return int(time.time() * 1000)

while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    if data:
        seq = byte82int(data[0:8])
        rt =  get_curr_time_ms() - byte82int(data[8:16])
        print('Received from %s, len is %d, seq is %d, rt is %f' % (addr, len(data), seq, rt))
        logging.debug('Received from %s, len is %d, seq is %d, rt is %f' % (addr, len(data), seq, rt))
        sent = s.sendto(data, addr)
        print('Send to %s, len is %d, seq is %d, rt is %f' % (addr, sent, seq, rt))
        logging.debug('Send to %s, len is %d, seq is %d, rt is %f' % (addr, sent, seq, rt))
