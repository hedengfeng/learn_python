#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 18:39
# @Author  : hedengfeng
# @Site    : 
# @File    : zmq_req0.py
# @Software: LearnPython

from time import sleep

import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.setsockopt(zmq.IDENTITY, b'0')
socket.connect("tcp://localhost:5559")
request = 0
while True:
    request = request + 1
    ident = b'req0'
    send_data1 = "req0 request"
    send_data2 = str(request)
    socket.send_multipart([ident, send_data1.encode(), send_data2.encode()])
    message = socket.recv_string()
    print("Received reply ", request, "[", message, "]")
    sleep(1)
